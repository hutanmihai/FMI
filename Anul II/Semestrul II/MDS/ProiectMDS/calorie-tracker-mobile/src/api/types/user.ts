export const USER_HEIGHT_METRIC = ['feet', 'cm'] as const;
export const USER_WEIGHT_METRIC = ['lbs', 'kg'] as const;

export type UserHeightMetric = (typeof USER_HEIGHT_METRIC)[number];
export type UserWeightMetric = (typeof USER_WEIGHT_METRIC)[number];

export interface User {
  id: string;
  g_id: string;
  email: string;
  picture?: string;
  name: string;
  pref_height_metric?: UserHeightMetric;
  height?: number;
  pref_weight_metric?: UserWeightMetric;
  weight?: number;
  target_weight?: number;
  target_calories?: number;
}
