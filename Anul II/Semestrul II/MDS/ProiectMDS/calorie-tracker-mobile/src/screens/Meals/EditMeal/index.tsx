import React, { useCallback, useEffect, useRef, useState } from 'react';

import { Components } from './styled';
import { useNavigation, useRoute } from '@react-navigation/native';
import { Product } from '../../../api/types/product';
import { Meal, MealProductBody } from '../../../api/types/meal';
import { COLORS } from '../../../utils/styled/constants';
import { apiFetch } from '../../../api';
import _ from 'lodash';
import InputComponent from '../../../components/InputComponent';
import { FlatList } from 'react-native';

const EditMeal = () => {
  const navigation = useNavigation();
  const meal = (useRoute().params as { meal: Meal }).meal;

  const [mealProducts, setMealProducts] = useState<Product[]>(meal.products);
  const [mealProductsBody, setMealProductsBody] = useState<MealProductBody[]>(
    meal.products.map((product) => {
      return {
        product_id: product.id,
        quantity_grams: product.quantity_grams,
      };
    }),
  );

  const [name, setName] = useState(meal.name);
  const [quantityGrams, setQuantityGrams] = useState('');

  const [products, setProducts] = useState<Product[]>([]);
  const [searchTerm, setSearchTerm] = useState('');
  const searchTermRef = useRef('');

  useEffect(() => {
    console.log('meal', meal);
  }, []);

  useEffect(() => {
    console.log('mealProducts', mealProducts);
  }, [mealProducts]);

  useEffect(() => {
    console.log('mealProductsBody', mealProductsBody);
  }, [mealProductsBody]);

  const _onSaveMeal = async () => {
    console.log({
      name: name || 'New Meal',
      products: mealProductsBody,
    });

    await apiFetch({
      path: `/meal/${meal.id}`,
      method: 'DELETE',
    });

    apiFetch({
      path: `/meal`,
      method: 'POST',
      body: {
        name: name || 'New Meal',
        products: mealProductsBody,
      },
    }).then((res) => {
      console.log(res);
      navigation.goBack();
    });
  };

  const onDebouncedSearch = async () => {
    console.log(searchTerm);
    apiFetch({
      path: `/product/search/${searchTermRef.current.toLowerCase()}`,
    }).then((data) => {
      setProducts(data?.products ?? ([] as Product[]));
    });
  };

  const searchHandler = useCallback(_.debounce(onDebouncedSearch, 1000), []);

  const onSearch = async (text: string) => {
    setSearchTerm(text);
    searchTermRef.current = text;
    await searchHandler();
  };

  const _onAddProduct = async (product: Product) => {
    const mealProductBody: MealProductBody = {
      product_id: product.id,
      quantity_grams: parseInt(quantityGrams) || 100,
    };

    setMealProducts([...mealProducts, product]);
    setMealProductsBody([...mealProductsBody, mealProductBody]);
    setSearchTerm('');
    setProducts([] as Product[]);
  };

  const _onRemoveProduct = async (product: Product) => {
    setMealProducts(mealProducts.filter((mealProduct) => mealProduct.id !== product.id));
    setMealProductsBody(mealProductsBody.filter((mealProduct) => mealProduct.product_id !== product.id));
  };

  const _renderAllProductsItem = useCallback(
    ({ item }: { item: Product }) => {
      return (
        <Components.ItemCell>
          <Components.Label>{item.name}</Components.Label>
          <Components.ItemCellFieldDescription
            color={COLORS.orange}>{`Carbs: ${item.carbs}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.lightGreen}>{`Protein: ${item.protein}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.blue}>{`Fat: ${item.fat}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={item.upvotes - item.downvotes >= 0 ? COLORS.green : COLORS.red}>
            Likes: {item.upvotes - item.downvotes}
          </Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper hasMinWidth={true}>
            {mealProducts.find((mealProduct) => mealProduct.id === item.id) === undefined ? (
              <Components.Button color={COLORS.green} onPress={() => _onAddProduct(item)}>
                <Components.ButtonLabel>Add</Components.ButtonLabel>
              </Components.Button>
            ) : (
              <Components.Button color={COLORS.red} onPress={() => _onRemoveProduct(item)}>
                <Components.ButtonLabel>Remove</Components.ButtonLabel>
              </Components.Button>
            )}
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [mealProducts, mealProductsBody, quantityGrams],
  );

  const _renderMealProductsItem = useCallback(
    ({ item }: { item: Product }) => {
      let itemQuantity =
        mealProductsBody.find((mealProduct) => mealProduct.product_id === item.id)?.quantity_grams ?? 100;

      return (
        <Components.ItemCell>
          <Components.Label>{item.name}</Components.Label>
          <Components.ItemCellFieldDescription color={COLORS.orange}>{`Carbs: ${
            (item.carbs * itemQuantity) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.lightGreen}>{`Protein: ${
            (item.protein * itemQuantity) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.blue}>{`Fat: ${
            (item.fat * itemQuantity) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.green}>
            Quantity: {mealProductsBody.find((mealProduct) => mealProduct.product_id === item.id)?.quantity_grams}g
          </Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper hasMinWidth={true}>
            <Components.Button color={COLORS.red} onPress={() => _onRemoveProduct(item)}>
              <Components.ButtonLabel>Remove</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [mealProductsBody, mealProducts],
  );

  return (
    <Components.Container>
      {products.length === 0 && (
        <InputComponent label={'Name'} placeholder={'Name...'} value={name} setValue={setName} />
      )}
      {products.length !== 0 && (
        <InputComponent
          label={'Quantity (g)'}
          placeholder={'100...'}
          value={quantityGrams}
          setValue={setQuantityGrams}
        />
      )}
      <InputComponent label={'Search for products'} placeholder={'Search...'} value={searchTerm} setValue={onSearch} />
      {products.length !== 0 && (
        <FlatList data={products} renderItem={_renderAllProductsItem} keyExtractor={(item) => item.id} />
      )}
      {products.length === 0 && mealProducts.length !== 0 && (
        <>
          <Components.ButtonsWrapper>
            <Components.Button color={COLORS.green} onPress={_onSaveMeal}>
              <Components.ButtonLabel>Save meal</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
          <FlatList data={mealProducts} renderItem={_renderMealProductsItem} keyExtractor={(item) => item.id} />
        </>
      )}
    </Components.Container>
  );
};

export default EditMeal;
