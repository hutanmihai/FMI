import React, { useCallback, useEffect, useRef, useState } from 'react';
import { Components } from './styled';
import _ from 'lodash';
import { Product, ProductVote } from '../../../api/types/product';
import { FlatList } from 'react-native';
import { apiFetch } from '../../../api';
import InputComponent from '../../../components/InputComponent';
import { COLORS } from '../../../utils/styled/constants';
import { useNavigation } from '@react-navigation/native';
import { faThumbsUp, faThumbsDown } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-native-fontawesome';
import AsyncStorage from '@react-native-async-storage/async-storage';

const Products = () => {
  // Navigation hooks
  const navigation = useNavigation();

  // Product related hooks
  const [products, setProducts] = useState<Product[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const searchTermRef = useRef('');
  const [productVotes, setProductVotes] = useState<ProductVote[]>([]);

  useEffect(() => {
    console.log('products', products);
  }, [products]);

  useEffect(() => {
    AsyncStorage.getItem('votes').then((votes) => {
      setProductVotes(JSON.parse(votes ?? '[]'));
    });
  }, []);

  useEffect(() => {
    console.log('productVotes', productVotes);
  }, [productVotes]);

  const navigateToCreateProduct = () => {
    // @ts-ignore
    navigation.navigate('Create Product');
  };

  // Search for products
  const onDebouncedSearch = async () => {
    console.log(searchTerm);
    apiFetch({
      path: `/product/search/${searchTermRef.current.toLowerCase()}`,
    }).then((data) => {
      setProducts(data?.products ?? ([] as Product[]));
    });
  };

  // Handler for debounced search ( 1000ms )
  const searchHandler = useCallback(_.debounce(onDebouncedSearch, 1000), []);

  // Set search term on input change
  const onSearch = async (text: string) => {
    setSearchTerm(text);
    searchTermRef.current = text;
    await searchHandler();
  };

  // Check if product should be deleted
  const checkVotes = async (item: Product) => {
    if (item.downvotes - item.upvotes >= 9) {
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'DELETE',
        isAdmin: true,
      });
    }
  };

  const checkIfUserVoted = (item: Product, vote: number) => {
    const userVote = productVotes.find((vote) => vote.id === item.id)?.vote;
    if (typeof userVote === 'number') {
      if (userVote === vote) {
        return vote === 1 ? 'UPVOTE' : 'DOWNVOTE';
      }

      return vote === 1 ? 'DOWNVOTE' : 'UPVOTE';
    }

    return 'NONE';
  };

  // Vote on a product
  const _onVote = async (item: Product, vote: number) => {
    const userVote = checkIfUserVoted(item, vote);

    if (userVote === 'UPVOTE' && vote === 1) {
      // Remove upvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          upvotes: item.upvotes - 1,
        },
      });

      setProductVotes(productVotes.filter((v) => v.id !== item.id));
      AsyncStorage.setItem('votes', JSON.stringify(productVotes.filter((v) => v.id !== item.id)));
    } else if (userVote === 'DOWNVOTE' && vote === 0) {
      // Remove downvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          downvotes: item.downvotes - 1,
        },
      });

      setProductVotes(productVotes.filter((v) => v.id !== item.id));
      AsyncStorage.setItem('votes', JSON.stringify(productVotes.filter((v) => v.id !== item.id)));
    } else if (userVote === 'DOWNVOTE' && vote === 1) {
      // Switch from downvote to upvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          upvotes: item.upvotes + 1,
          downvotes: item.downvotes - 1,
        },
      });

      setProductVotes(productVotes.map((v) => (v.id === item.id ? { ...v, vote: 1 } : v)));
      AsyncStorage.setItem(
        'votes',
        JSON.stringify(productVotes.map((v) => (v.id === item.id ? { ...v, vote: 1 } : v))),
      );
    } else if (userVote === 'UPVOTE' && vote === 0) {
      // Switch from upvote to downvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          upvotes: item.upvotes - 1,
          downvotes: item.downvotes + 1,
        },
      });

      setProductVotes(productVotes.map((v) => (v.id === item.id ? { ...v, vote: 0 } : v)));
      AsyncStorage.setItem(
        'votes',
        JSON.stringify(productVotes.map((v) => (v.id === item.id ? { ...v, vote: 0 } : v))),
      );
    } else if (userVote === 'NONE' && vote === 1) {
      // Add upvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          upvotes: item.upvotes + 1,
        },
      });

      setProductVotes([...productVotes, { id: item.id, vote: 1 }]);
    } else if (userVote === 'NONE' && vote === 0) {
      // Add downvote
      await apiFetch({
        path: `/product/${item.id}`,
        method: 'PUT',
        body: {
          downvotes: item.downvotes + 1,
        },
      });

      setProductVotes([...productVotes, { id: item.id, vote: 0 }]);
    }

    await checkVotes(item);
    await onDebouncedSearch();
  };

  // Render function for FlatList
  const _renderItem = useCallback(
    ({ item }: { item: Product }) => {
      const isProductUpvotedByUser = productVotes.find((vote) => vote.id === item.id)?.vote;

      return (
        <Components.ItemCell>
          <Components.Label>{item.name}</Components.Label>
          <Components.ItemCellFieldDescription
            color={COLORS.orange}>{`Carbs: ${item.carbs}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.lightGreen}>{`Protein: ${item.protein}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.blue}>{`Fat: ${item.fat}g`}</Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper>
            <Components.ItemCellFieldDescription color={item.upvotes - item.downvotes >= 0 ? COLORS.green : COLORS.red}>
              Likes: {item.upvotes - item.downvotes}
            </Components.ItemCellFieldDescription>
            <Components.ItemCellDetails>
              <Components.Button onPress={() => _onVote(item, 1)}>
                <FontAwesomeIcon
                  icon={faThumbsUp}
                  size={20}
                  color={
                    typeof isProductUpvotedByUser === 'number' && isProductUpvotedByUser ? COLORS.green : COLORS.white
                  }
                />
              </Components.Button>
              <Components.Button onPress={() => _onVote(item, 0)}>
                <FontAwesomeIcon
                  icon={faThumbsDown}
                  size={20}
                  color={
                    typeof isProductUpvotedByUser === 'number' && !isProductUpvotedByUser ? COLORS.red : COLORS.white
                  }
                />
              </Components.Button>
            </Components.ItemCellDetails>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [productVotes],
  );

  return (
    <Components.Container>
      {products.length === 0 && (
        <Components.ButtonsWrapper>
          <Components.CreateButton onPress={() => navigateToCreateProduct()}>
            <Components.ButtonLabel>Create product</Components.ButtonLabel>
          </Components.CreateButton>
        </Components.ButtonsWrapper>
      )}
      <InputComponent label={'Search for products'} placeholder={'Search...'} value={searchTerm} setValue={onSearch} />
      <FlatList data={products} renderItem={_renderItem} keyExtractor={(item) => item.id} />
    </Components.Container>
  );
};

export default Products;
