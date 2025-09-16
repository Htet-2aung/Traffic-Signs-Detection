# master_map.py

# Unified class list: 80 unique traffic sign categories from GTSRB (43 classes) and VNTS (58 classes).
# Similar signs are merged (e.g., all "speed_limit" variants into one class, "stop" from both datasets).
unified_classes = [
    'speed_limit', 'end_speed_limit', 'no_passing', 'no_heavy_vehicles', 'priority_road', 'yield', 'stop',
    'no_vehicles', 'vehicles_over_tons_prohibited', 'no_entry', 'general_caution', 'curve_left', 'curve_right',
    'double_curve', 'bumpy_road', 'slippery_road', 'road_narrows', 'road_work', 'traffic_signals', 'pedestrians',
    'children_crossing', 'bicycles_crossing', 'ice_snow', 'wild_animals', 'end_limits', 'turn_right_ahead',
    'turn_left_ahead', 'ahead_only', 'straight_or_right', 'straight_or_left', 'keep_right', 'keep_left',
    'roundabout', 'speed_bump', 'sharp_deviation', 'crossroad', 'falling_rocks', 'ferry_terminal', 'one_way',
    'two_way_traffic', 'steep_hill', 'railway_crossing', 'tramway_crossing', 'traffic_queues', 'low_flying_aircraft',
    'crosswind', 'tunnel', 'other_danger', 'no_cycles', 'no_goods_vehicles', 'no_pedestrians', 'no_bullock_carts',
    'no_hand_carts', 'no_motor_vehicles', 'height_limit', 'weight_limit', 'axle_weight_limit', 'length_limit',
    'no_left_turn', 'no_right_turn', 'horn_prohibited', 'no_parking', 'no_stopping', 'steep_descent',
    'steep_ascent', 'narrow_bridge', 'unprotected_quay', 'dip', 'loose_gravel', 'cattle', 'side_road_junction',
    'oblique_side_road_junction', 't_junction', 'y_junction', 'staggered_side_road_junction',
    'guarded_level_crossing', 'unguarded_level_crossing', 'level_crossing_countdown', 'parking', 'bus_stop',
    'first_aid_post', 'telephone', 'filling_station', 'hotel', 'restaurant', 'refreshments'
]

nc = len(unified_classes)  # 80 unique classes

# Master map: Maps original dataset IDs to unified class IDs
master_map = {
    'gtsrb': {
        0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 1, 7: 0, 8: 0, 9: 2, 10: 3, 11: 4, 12: 5, 13: 5, 14: 6,
        15: 7, 16: 3, 17: 9, 18: 10, 19: 11, 20: 12, 21: 13, 22: 14, 23: 15, 24: 16, 25: 17, 26: 18,
        27: 19, 28: 20, 29: 21, 30: 22, 31: 23, 32: 24, 33: 25, 34: 26, 35: 27, 36: 28, 37: 29, 38: 30,
        39: 31, 40: 32, 41: 1, 42: 1
    },
    'vnts': {
        0: 33, 1: 10, 2: 11, 3: 12, 4: 13, 5: 34, 6: 25, 7: 26, 8: 28, 9: 35, 10: 0, 11: 24, 12: 4,
        13: 4, 14: 19, 15: 19, 16: 19, 17: 20, 18: 21, 19: 18, 20: 17, 21: 23, 22: 36, 23: 37, 24: 3,
        25: 3, 26: 3, 27: 2, 28: 27, 29: 6, 30: 38, 31: 24, 32: 30, 33: 0, 34: 32, 35: 11, 36: 12,
        37: 39, 38: 39, 39: 35, 40: 35, 41: 14, 42: 14, 43: 14, 44: 15, 45: 15, 46: 15, 47: 16,
        48: 22, 49: 40, 50: 41, 51: 42, 52: 43, 53: 44, 54: 45, 55: 46, 56: 47, 57: 37
    }
}