import React, { useContext, useEffect, useState } from 'react';
import { Components } from './styled';
import { COLORS } from '../../../utils/styled/constants';
import { AuthContext } from '../../../providers/AuthProvider/context';
import { useIsFocused, useNavigation } from '@react-navigation/native';

import PieChart from 'react-native-pie-chart';
import { SCREEN_WIDTH } from '../../../utils/dimensions';
import { Diary } from '../../../api/types/diary';
import { apiFetch } from '../../../api';
import { format } from 'date-fns';
import * as Progress from 'react-native-progress';

const Home = () => {
  // Navigation variables
  const navigation = useNavigation();
  const isFocused = useIsFocused();

  const { user } = useContext(AuthContext);

  // State to store the current diary
  const [currentDiary, setCurrentDiary] = useState<Diary | null>(null);

  // When the screen is focused, fetch the current diary
  useEffect(() => {
    if (!isFocused) {
      return;
    }

    apiFetch({
      path: '/diaries',
    }).then((response) => {
      setCurrentDiary((response as Diary[]).filter((diary) => diary.date === format(new Date(), 'yyyy-MM-dd'))?.[0]);
    });
  }, [isFocused]);

  useEffect(() => {
    console.log('currentDiary', currentDiary);
  }, [currentDiary]);

  return (
    <Components.Container>
      <Components.TextContainer>
        <Components.WelcomeText>{`Welcome, ${user?.name ?? 'User'}!`}</Components.WelcomeText>
        <Components.TargetText>{`${((user?.target_calories ?? 2000) - (currentDiary?.total_calories ?? 0)).toFixed(
          2,
        )} calories left until you reach your target of ${
          user?.target_calories ?? 2000
        } calories`}</Components.TargetText>
        <Progress.Bar
          progress={Math.min((currentDiary?.total_calories ?? 0) / (user?.target_calories ?? 2000), 1)}
          width={SCREEN_WIDTH - 40}
          color={COLORS.orange}
        />
        <Components.TargetText>{`${Math.abs((user?.target_weight ?? 80) - (user?.weight ?? 80)).toFixed(
          2,
        )}kg left until you reach your target of ${user?.target_weight ?? 80}kg`}</Components.TargetText>
        <Progress.Bar
          progress={
            Math.min(user?.weight ?? 80, user?.target_weight ?? 80) /
            Math.max(user?.weight ?? 80, user?.target_weight ?? 80)
          }
          width={SCREEN_WIDTH - 40}
          color={COLORS.blue}
          unfilledColor={(user?.weight ?? 80) > (user?.target_weight ?? 80) ? COLORS.red : COLORS.lightGreen}
          borderWidth={0}
        />
      </Components.TextContainer>
      <Components.PieChartWrapper>
        <Components.CaloriesText offset={'42%'}>Calories</Components.CaloriesText>
        <Components.CaloriesText offset={'35%'}>{currentDiary?.total_calories ?? 0}</Components.CaloriesText>
        <PieChart
          widthAndHeight={SCREEN_WIDTH / 2}
          series={[currentDiary?.total_carbs ?? 0, currentDiary?.total_protein ?? 0, currentDiary?.total_fat ?? 1]}
          sliceColor={[COLORS.orange, COLORS.lightGreen, COLORS.blue]}
          coverRadius={0.9}
          coverFill={COLORS.black}
        />
        <Components.AdditionalInfo color={COLORS.orange} offset={'80%'}>
          {`Carbs: ${currentDiary?.total_carbs ?? 0}g`}
        </Components.AdditionalInfo>
        <Components.AdditionalInfo color={COLORS.lightGreen} offset={'87%'}>
          {`Protein: ${currentDiary?.total_protein ?? 0}g`}
        </Components.AdditionalInfo>
        <Components.AdditionalInfo color={COLORS.blue} offset={'94%'}>
          {`Fat: ${currentDiary?.total_fat ?? 0}g`}
        </Components.AdditionalInfo>
      </Components.PieChartWrapper>

      <Components.ButtonsWrapper>
        {/*@ts-ignore*/}
        <Components.Button onPress={() => navigation.navigate('Diaries')}>
          <Components.ButtonLabel>{'Diary'}</Components.ButtonLabel>
        </Components.Button>
        {/*@ts-ignore*/}
        <Components.Button onPress={() => navigation.navigate('Meals')}>
          <Components.ButtonLabel>{'Meals'}</Components.ButtonLabel>
        </Components.Button>
        {/*@ts-ignore*/}
        <Components.Button onPress={() => navigation.navigate('Products')}>
          <Components.ButtonLabel>{'Products'}</Components.ButtonLabel>
        </Components.Button>
        {/*@ts-ignore*/}
        <Components.Button onPress={() => navigation.navigate('Account')}>
          <Components.ButtonLabel>{'Account'}</Components.ButtonLabel>
        </Components.Button>
      </Components.ButtonsWrapper>
    </Components.Container>
  );
};

export default Home;
