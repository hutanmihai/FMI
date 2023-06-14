import React, { useCallback, useEffect, useRef, useState } from 'react';

import { Components } from './styled';
import { useNavigation, useRoute } from '@react-navigation/native';
import { Product } from '../../../api/types/product';
import { COLORS } from '../../../utils/styled/constants';
import { apiFetch } from '../../../api';
import _ from 'lodash';
import InputComponent from '../../../components/InputComponent';
import { FlatList } from 'react-native';
import { Diary, DiaryProductBody } from '../../../api/types/diary';
import { Meal } from '../../../api/types/meal';

const EditDiary = () => {
  const navigation = useNavigation();
  const diary = (useRoute().params as { diary: Diary }).diary;

  const [diaryProducts, setDiaryProducts] = useState<Product[]>(diary.products);
  const [diaryProductsBody, setDiaryProductsBody] = useState<DiaryProductBody[]>(
    diary.products.map((product) => {
      return {
        product_id: product.id,
        quantity_grams: product.quantity_grams,
      };
    }),
  );
  const [diaryDate] = useState(diary.date);

  const [quantityGrams, setQuantityGrams] = useState('');

  const [products, setProducts] = useState<Product[]>([]);
  const [meals, setMeals] = useState<Meal[]>([]);
  const [filteredMeals, setFilteredMeals] = useState<Meal[]>([]);

  const [searchProductsTerm, setSearchProductsTerm] = useState('');
  const searchProductsTermRef = useRef('');

  const [searchMealsTerm, setSearchMealsTerm] = useState('');
  const searchMealsTermRef = useRef('');

  useEffect(() => {
    apiFetch({
      path: '/meals',
    }).then((data) => {
      setMeals(data);
    });
  }, []);

  useEffect(() => {
    console.log('diaryProducts', diaryProducts);
  }, [diaryProducts]);

  useEffect(() => {
    console.log('diaryProductsBody', diaryProductsBody);
  }, [diaryProductsBody]);

  useEffect(() => {
    console.log('products', products);
  }, [products]);

  useEffect(() => {
    console.log('meals', meals);
  }, [meals]);

  useEffect(() => {
    console.log('filteredMeals', filteredMeals);
  }, [filteredMeals]);

  const _onSaveDiary = async () => {
    console.log({
      date: diaryDate,
      products: diaryProductsBody,
    });

    await apiFetch({
      path: `/diary/${diary.id}`,
      method: 'DELETE',
    });

    apiFetch({
      path: `/diary`,
      method: 'POST',
      body: {
        date: diaryDate,
        products: diaryProductsBody.map((diaryProduct) => {
          return {
            product_id: diaryProduct.product_id,
            quantity_grams: diaryProduct.quantity_grams,
          };
        }),
      },
    }).then((res) => {
      console.log(res);
      navigation.goBack();
    });
  };

  const onDebouncedProductsSearch = async () => {
    apiFetch({
      path: `/product/search/${searchProductsTermRef.current.toLowerCase()}`,
    }).then((data) => {
      setProducts(data?.products ?? ([] as Product[]));
    });
  };

  const onDebouncedMealsSearch = async () => {
    if (searchMealsTermRef.current.trim() === '') {
      setFilteredMeals([] as Meal[]);
      return;
    }

    setFilteredMeals(
      meals.filter((meal) => {
        return meal.name.toLowerCase().includes(searchMealsTermRef.current.trim().toLowerCase());
      }),
    );
  };

  const searchProductsHandler = useCallback(_.debounce(onDebouncedProductsSearch, 1000), []);

  const searchMealsHandler = useCallback(_.debounce(onDebouncedMealsSearch, 1000), [meals]);

  const onSearchProducts = async (text: string) => {
    setSearchProductsTerm(text);
    searchProductsTermRef.current = text;
    await searchProductsHandler();
  };

  const onSearchMeals = async (text: string) => {
    setSearchMealsTerm(text);
    searchMealsTermRef.current = text;
    await searchMealsHandler();
  };

  const _onAddProductToDiary = async (product: Product) => {
    const diaryProductBody: DiaryProductBody = {
      product_id: product.id,
      quantity_grams: parseInt(quantityGrams) || 100,
    };

    setDiaryProducts([...diaryProducts, product]);
    setDiaryProductsBody([...diaryProductsBody, diaryProductBody]);
    setSearchProductsTerm('');
    setProducts([] as Product[]);
  };

  const _onRemoveProductFromDiary = async (product: Product) => {
    setDiaryProducts(diaryProducts.filter((diaryProduct) => diaryProduct.id !== product.id));
    setDiaryProductsBody(diaryProductsBody.filter((diaryProduct) => diaryProduct.product_id !== product.id));
  };

  const _onAddMealToDiary = async (meal: Meal) => {
    let _diaryProducts: Product[] = [];
    let _diaryProductsBody: DiaryProductBody[] = [];
    meal.products.forEach((product) => {
      if (diaryProducts.find((diaryProduct) => diaryProduct.id === product.id) === undefined) {
        const diaryProductBody: DiaryProductBody = {
          product_id: product.id,
          quantity_grams: product.quantity_grams,
          is_from_meal: true,
        };

        console.log('diaryProductBody', diaryProductBody);

        _diaryProducts.push(product);
        _diaryProductsBody.push(diaryProductBody);
      } else {
        _diaryProductsBody = _diaryProductsBody.map((diaryProduct) => {
          if (diaryProduct.product_id === product.id) {
            return {
              ...diaryProduct,
              quantity_grams: diaryProduct.quantity_grams + product.quantity_grams,
            };
          }

          return diaryProduct;
        });
      }
    });

    setDiaryProducts([...diaryProducts, ..._diaryProducts]);
    setDiaryProductsBody([...diaryProductsBody, ..._diaryProductsBody]);
    setSearchMealsTerm('');
    setFilteredMeals([] as Meal[]);
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
            {diaryProducts.find((diaryProduct) => diaryProduct.id === item.id) === undefined ? (
              <Components.Button color={COLORS.green} onPress={() => _onAddProductToDiary(item)}>
                <Components.ButtonLabel>Add</Components.ButtonLabel>
              </Components.Button>
            ) : (
              <Components.Button color={COLORS.red} onPress={() => _onRemoveProductFromDiary(item)}>
                <Components.ButtonLabel>Remove</Components.ButtonLabel>
              </Components.Button>
            )}
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [diaryProducts, diaryProductsBody, quantityGrams],
  );

  const _renderAllMeals = useCallback(
    ({ item }: { item: Meal }) => {
      return (
        <Components.ItemCell>
          <Components.Label>{item.name}</Components.Label>
          <Components.ItemCellFieldDescription
            color={COLORS.orange}>{`Carbs: ${item.total_carbs}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.lightGreen}>{`Protein: ${item.total_protein}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription
            color={COLORS.blue}>{`Fat: ${item.total_fat}g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.green}>{`Products: ${item.products
            .map((product: Product) => product.name)
            .join(' | ')}`}</Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper hasMinWidth={true}>
            <Components.Button color={COLORS.green} onPress={() => _onAddMealToDiary(item)}>
              <Components.ButtonLabel>Add All</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [meals],
  );

  const _renderDiaryProductsItem = useCallback(
    ({ item }: { item: Product }) => {
      let isCurrentItemFromMeal = !!diaryProductsBody.find((diaryProduct) => diaryProduct.product_id === item.id)
        ?.is_from_meal;
      let itemQuantityGrams =
        diaryProductsBody.find((diaryProduct) => diaryProduct.product_id === item.id)?.quantity_grams ?? 100;

      return (
        <Components.ItemCell>
          <Components.Label>{item.name}</Components.Label>
          <Components.ItemCellFieldDescription color={COLORS.orange}>{`Carbs: ${
            isCurrentItemFromMeal ? item.carbs : (item.carbs * itemQuantityGrams) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.lightGreen}>{`Protein: ${
            isCurrentItemFromMeal ? item.protein : (item.protein * itemQuantityGrams) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.blue}>{`Fat: ${
            isCurrentItemFromMeal ? item.fat : (item.fat * itemQuantityGrams) / 100
          }g`}</Components.ItemCellFieldDescription>
          <Components.ItemCellFieldDescription color={COLORS.green}>
            Quantity: {diaryProductsBody.find((diaryProduct) => diaryProduct.product_id === item.id)?.quantity_grams}g
          </Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper hasMinWidth={true}>
            <Components.Button color={COLORS.red} onPress={() => _onRemoveProductFromDiary(item)}>
              <Components.ButtonLabel>Remove</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [diaryProductsBody, diaryProducts],
  );

  return (
    <Components.Container>
      {filteredMeals.length == 0 && (
        <InputComponent
          label={'Quantity (g)'}
          placeholder={'100...'}
          value={quantityGrams}
          setValue={setQuantityGrams}
        />
      )}
      {products?.length == 0 && quantityGrams.trim() === '' && (
        <InputComponent
          label={'Search for meals'}
          placeholder={'Search...'}
          value={searchMealsTerm}
          setValue={onSearchMeals}
        />
      )}

      {filteredMeals.length == 0 && (
        <InputComponent
          label={'Search for products'}
          placeholder={'Search...'}
          value={searchProductsTerm}
          setValue={onSearchProducts}
        />
      )}
      {products?.length !== 0 && (
        <FlatList data={products} renderItem={_renderAllProductsItem} keyExtractor={(item) => item.id} />
      )}
      {filteredMeals.length !== 0 && (
        <FlatList data={filteredMeals} renderItem={_renderAllMeals} keyExtractor={(item) => item.id} />
      )}
      {products?.length === 0 && diaryProducts?.length !== 0 && filteredMeals?.length === 0 && (
        <>
          <Components.ButtonsWrapper>
            <Components.Button color={COLORS.green} onPress={_onSaveDiary}>
              <Components.ButtonLabel>Save Diary</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
          <FlatList data={diaryProducts} renderItem={_renderDiaryProductsItem} keyExtractor={(item) => item.id} />
        </>
      )}
    </Components.Container>
  );
};

export default EditDiary;
