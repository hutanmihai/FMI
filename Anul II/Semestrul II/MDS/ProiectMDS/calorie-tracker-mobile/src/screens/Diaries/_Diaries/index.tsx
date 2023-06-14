import React, { useCallback, useEffect, useState } from 'react';
import { Components } from './styled';
import { COLORS } from '../../../utils/styled/constants';
import { useIsFocused, useNavigation } from '@react-navigation/native';
import { apiFetch } from '../../../api';
import { Product } from '../../../api/types/product';
import { FlatList } from 'react-native';
import { Diary } from '../../../api/types/diary';
import { format } from 'date-fns';
import DatePicker from 'react-native-date-picker';

const Diaries = () => {
  const navigation = useNavigation();
  const isFocused = useIsFocused();

  const [allDiaries, setAllDiaries] = useState<Diary[]>([]);
  const [diaries, setDiaries] = useState<Diary[]>([]);
  const [currentDate] = useState<Date>(new Date());
  const [date, setDate] = useState<Date>(new Date());
  const [isDatePickerVisible, setIsDatePickerVisible] = useState(false);

  // Refresh diaries on focus
  useEffect(() => {
    if (!isFocused) {
      return;
    }

    apiFetch({
      path: '/diaries',
    }).then((data) => {
      setAllDiaries(data);
      setDiaries(data.filter((diary: Diary) => diary.date === format(currentDate, 'yyyy-MM-dd')));
    });
  }, [isFocused]);

  useEffect(() => {
    setDiaries(allDiaries.filter((diary: Diary) => diary.date === format(date, 'yyyy-MM-dd')));
  }, [date]);

  useEffect(() => {
    console.log('diaries', diaries);
  }, [diaries]);

  const navigateToCreateDiary = () => {
    // @ts-ignore
    navigation.navigate('Create Diary');
  };

  const _editDiary = async (diary: Diary) => {
    // @ts-ignore
    navigation.navigate('Edit Diary', { diary });
  };

  const _deleteDiary = async (diary: Diary) => {
    await apiFetch({
      path: `/diary/${diary.id}`,
      method: 'DELETE',
    });

    setDiaries(diaries.filter((item) => item.id !== diary.id));
  };

  const _onConfirmDateSelection = (newDate: Date) => {
    setIsDatePickerVisible(false);
    setDate(newDate);
  };

  const _onCancelDateSelection = () => {
    setIsDatePickerVisible(false);
  };

  const _renderItem = useCallback(
    ({ item }: { item: Diary }) => {
      return (
        <Components.ItemCell>
          <Components.Label>
            {item?.date === format(currentDate, 'yyyy-MM-dd')
              ? "Today's Diary"
              : `Diary from ${format(date, 'yyyy MMM dd')}`}
          </Components.Label>
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
            <Components.Button color={COLORS.blue} onPress={() => _editDiary(item)}>
              <Components.ButtonLabel>Edit</Components.ButtonLabel>
            </Components.Button>
            <Components.Button color={COLORS.red} onPress={() => _deleteDiary(item)}>
              <Components.ButtonLabel>Remove</Components.ButtonLabel>
            </Components.Button>
          </Components.ButtonsWrapper>
        </Components.ItemCell>
      );
    },
    [diaries],
  );

  return (
    <Components.Container>
      <Components.ButtonsWrapper>
        <Components.Button color={COLORS.green} onPress={() => setIsDatePickerVisible(true)}>
          <Components.ButtonLabel>{'Change date'}</Components.ButtonLabel>
        </Components.Button>
      </Components.ButtonsWrapper>
      <DatePicker
        modal
        date={date}
        maximumDate={currentDate}
        mode={'date'}
        onDateChange={setDate}
        open={isDatePickerVisible}
        onConfirm={_onConfirmDateSelection}
        onCancel={_onCancelDateSelection}
      />
      {diaries.length === 0 && date.toDateString() === currentDate.toDateString() && (
        <Components.ButtonsWrapper>
          <Components.Button color={COLORS.green} onPress={() => navigateToCreateDiary()}>
            <Components.ButtonLabel>{'Create diary'}</Components.ButtonLabel>
          </Components.Button>
        </Components.ButtonsWrapper>
      )}
      {diaries.length === 0 && (
        <Components.CreateDiaryText>{`You have no diary for ${
          currentDate.toDateString() === date.toDateString() ? 'today.' : format(date, 'yyyy MMM dd') + '.'
        }`}</Components.CreateDiaryText>
      )}
      <FlatList data={diaries} renderItem={_renderItem} keyExtractor={(item) => item.id} />
    </Components.Container>
  );
};

export default Diaries;
