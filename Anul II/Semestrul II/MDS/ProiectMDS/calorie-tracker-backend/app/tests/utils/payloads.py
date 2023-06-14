from app.apis.utils.enums import HeightMetric, WeightMetric


def get_update_user_payload(
    name: str | None,
    pref_height_metric: HeightMetric | None,
    pref_weight_metric: WeightMetric | None,
    height: float | None,
    weight: float | None,
    target_weight: float | None,
    target_calories: int | None,
):
    payload = {}
    if name is not None:
        payload["name"] = name
    if pref_height_metric is not None:
        payload["pref_height_metric"] = pref_height_metric
    if pref_weight_metric is not None:
        payload["pref_weight_metric"] = pref_weight_metric
    if height is not None:
        payload["height"] = height
    if weight is not None:
        payload["weight"] = weight
    if target_weight is not None:
        payload["target_weight"] = target_weight
    if target_calories is not None:
        payload["target_calories"] = target_calories
    return payload


def get_create_product_payload(
    name: str | None,
    calories: float | None,
    fat: float | None,
    protein: float | None,
    carbs: float | None,
):
    payload = {}
    if name is not None:
        payload["name"] = name
    if calories is not None:
        payload["calories"] = calories
    if fat is not None:
        payload["fat"] = fat
    if protein is not None:
        payload["protein"] = protein
    if carbs is not None:
        payload["carbs"] = carbs
    return payload


def get_update_product_payload(
    name: str | None,
    calories: float | None,
    fat: float | None,
    protein: float | None,
    carbs: float | None,
    upvotes: int | None,
    downvotes: int | None,
):
    payload = {}
    if name is not None:
        payload["name"] = name
    if calories is not None:
        payload["calories"] = calories
    if fat is not None:
        payload["fat"] = fat
    if protein is not None:
        payload["protein"] = protein
    if carbs is not None:
        payload["carbs"] = carbs
    if upvotes is not None:
        payload["upvotes"] = upvotes
    if downvotes is not None:
        payload["downvotes"] = downvotes
    return payload
