import React, { useCallback, useEffect, useState } from 'react';
import { Components } from './styled';
import { COLORS } from '../../../utils/styled/constants';
import { useIsFocused, useNavigation } from '@react-navigation/native';
import { Meal } from '../../../api/types/meal';
import { apiFetch } from '../../../api';
import { Product } from '../../../api/types/product';
import { FlatList } from 'react-native';

const Meals = () => {
  const navigation = useNavigation();
  const isFocused = useIsFocused();

  const [meals, setMeals] = useState<Meal[]>([]);

  // Refresh meals on focus
  useEffect(() => {
    console.log(isFocused);
    if (!isFocused) {
      return;
    }

    apiFetch({
      path: '/meals',
    }).then((data) => {
      console.log(data);
      setMeals(data);
    });
  }, [isFocused]);

  useEffect(() => {
    console.log('meals', meals);
  }, [meals]);

  const navigateToCreateMeal = () => {
    // @ts-ignore
    navigation.navigate('Create Meal');
  };

  const _deleteMeal = async (meal: Meal) => {
    await apiFetch({
      path: `/meal/${meal.id}`,
      method: 'DELETE',
    });

    setMeals(meals.filter((item) => item.id !== meal.id));
  };

  const _editMeal = async (meal: Meal) => {
    // @ts-ignore
    navigation.navigate('Edit Meal', { meal });
  };

  const _renderItem = useCallback(
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
            .map((product: Product) => '\n   • ' + product.name)
            .join('')}`}</Components.ItemCellFieldDescription>
          <Components.ButtonsWrapper hasMinwidth={true}>
            <Components.Button color={COLORS.blue} onPress={() => _editMeal(item)}>
              <Components.ButtonLabel>Edit</Components.ButtonLabel>
            </Components.Button>
            <Components.Button color={COLORS.red} onPress={() => _deleteMeal(item)}>
              <Components.ButtonLabel>Delete</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [meals],
  );

  return (
    <Components.Container>
      <Components.ButtonsWrapper>
        <Components.Button color={COLORS.green} onPress={() => navigateToCreateMeal()}>
          <Components.ButtonLabel>Create meal</Components.ButtonLabel>
        </Components.Button>
      </Components.ButtonsWrapper>
      <FlatList data={meals} renderItem={_renderItem} keyExtractor={(item) => item.id} />
    </Components.Container>
  );
};

export default Meals;
