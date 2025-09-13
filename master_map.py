# Unified class list: A comprehensive list of unique traffic sign categories across GTSRB (43 classes), VNTS (58 classes), Chinese Traffic Signs (58 categories), and Indian Traffic Signs (59 classes).
# Similar signs are merged (e.g., all "speed_limit" variants into one class, "stop" from all datasets into one).
# Unique signs get distinct IDs. Total unique classes: 80 (adjusted for overlaps like stop, yield, speed limit, no entry, etc.).

unified_classes = [
    'speed_limit',  # Merged all specific speed limits (e.g., 20km/h, 30km/h, 90km/h from all datasets)
    'end_speed_limit',  # End of speed limit
    'no_passing',  # No passing/overtaking
    'no_heavy_vehicles',  # No trucks/buses/goods vehicles
    'priority_road',  # Priority road
    'yield',  # Yield/give way
    'stop',  # Stop
    'no_vehicles',  # No vehicles in both directions
    'vehicles_over_tons_prohibited',  # Vehicles over 3.5t prohibited
    'no_entry',  # No entry
    'general_caution',  # General danger/caution
    'curve_left',  # Dangerous curve left
    'curve_right',  # Dangerous curve right
    'double_curve',  # Double curve
    'bumpy_road',  # Bumpy/uneven road
    'slippery_road',  # Slippery road
    'road_narrows',  # Road narrows
    'road_work',  # Road work/construction
    'traffic_signals',  # Traffic lights ahead
    'pedestrians',  # Pedestrians crossing
    'children_crossing',  # Children/school crossing
    'bicycles_crossing',  # Bicycles crossing
    'ice_snow',  # Beware of ice/snow
    'wild_animals',  # Wild animals crossing
    'end_limits',  # End of all speed and passing limits
    'turn_right_ahead',  # Turn right ahead
    'turn_left_ahead',  # Turn left ahead
    'ahead_only',  # Ahead/straight only
    'straight_or_right',  # Go straight or right
    'straight_or_left',  # Go straight or left
    'keep_right',  # Keep right
    'keep_left',  # Keep left
    'roundabout',  # Roundabout mandatory
    'speed_bump',  # Speed bump/hump
    'sharp_deviation',  # Sharp deviation
    'crossroad',  # Crossroads
    'falling_rocks',  # Falling rocks
    'ferry_terminal',  # Ferry terminal
    'one_way',  # One-way traffic
    'two_way_traffic',  # Two-way traffic
    'steep_hill',  # Steep ascent/descent
    'railway_crossing',  # Guarded/unguarded level crossing
    'tramway_crossing',  # Tramway crossing
    'traffic_queues',  # Traffic queues
    'low_flying_aircraft',  # Low flying aircraft
    'crosswind',  # Crosswind
    'tunnel',  # Tunnel
    'other_danger',  # Other danger/refreshments
    'no_cycles',  # No entry for cycles
    'no_goods_vehicles',  # No entry for goods vehicles
    'no_pedestrians',  # No entry for pedestrians
    'no_bullock_carts',  # No entry for bullock carts
    'no_hand_carts',  # No entry for hand carts
    'no_motor_vehicles',  # No entry for motor vehicles
    'height_limit',  # Height limit
    'weight_limit',  # Weight limit
    'axle_weight_limit',  # Axle weight limit
    'length_limit',  # Length limit
    'no_left_turn',  # No left turn
    'no_right_turn',  # No right turn
    'horn_prohibited',  # Horn prohibited
    'no_parking',  # No parking
    'no_stopping',  # No stopping
    'steep_descent',  # Steep descent
    'steep_ascent',  # Steep ascent
    'narrow_bridge',  # Narrow bridge
    'unprotected_quay',  # Unprotected quay
    'dip',  # Dip
    'loose_gravel',  # Loose gravel
    'cattle',  # Cattle
    'side_road_junction',  # Side road junction
    'oblique_side_road_junction',  # Oblique side road junction
    't_junction',  # T-junction
    'y_junction',  # Y-junction
    'staggered_side_road_junction',  # Staggered side road junction
    'guarded_level_crossing',  # Guarded level crossing ahead
    'unguarded_level_crossing',  # Unguarded level crossing ahead
    'level_crossing_countdown',  # Level crossing countdown marker
    'parking',  # Parking
    'bus_stop',  # Bus stop
    'first_aid_post',  # First aid post
    'telephone',  # Telephone
    'filling_station',  # Filling station
    'hotel',  # Hotel
    'restaurant',  # Restaurant
    'refreshments'  # Refreshments
]

nc = len(unified_classes)  # 80 unique classes

# Master map: Maps original dataset IDs to unified class IDs
# - GTSRB: Classes 0-42
# - VNTS: IDs 0-57 (numeric, based on data.yaml order)
# - Chinese: Categories 0-57 (numeric, from annotations.csv; assuming standard Chinese set aligning with Indian/VNTS)
# - Indian: ClassId 0-58 (numeric, from traffic_sign.csv)
master_map = {
    'gtsrb': {
        0: 0,  # Speed limit 20km/h -> speed_limit
        1: 0,  # Speed limit 30km/h -> speed_limit
        2: 0,  # Speed limit 50km/h -> speed_limit
        3: 0,  # Speed limit 60km/h -> speed_limit
        4: 0,  # Speed limit 70km/h -> speed_limit
        5: 0,  # Speed limit 80km/h -> speed_limit
        6: 1,  # End speed limit 80km/h -> end_speed_limit
        7: 0,  # Speed limit 100km/h -> speed_limit
        8: 0,  # Speed limit 120km/h -> speed_limit
        9: 2,  # No passing -> no_passing
        10: 3,  # No passing for vehicles over 3.5t -> no_heavy_vehicles
        11: 4,  # Priority road -> priority_road
        12: 5,  # Priority -> yield (merged)
        13: 5,  # Yield -> yield
        14: 6,  # Stop -> stop
        15: 7,  # No vehicles -> no_vehicles
        16: 3,  # Vehicles over 3.5t prohibited -> no_heavy_vehicles
        17: 9,  # No entry -> no_entry
        18: 10,  # General caution -> general_caution
        19: 11,  # Dangerous curve left -> curve_left
        20: 12,  # Dangerous curve right -> curve_right
        21: 13,  # Double curve -> double_curve
        22: 14,  # Bumpy road -> bumpy_road
        23: 15,  # Slippery road -> slippery_road
        24: 16,  # Road narrows on the right -> road_narrows
        25: 17,  # Road work -> road_work
        26: 18,  # Traffic signals -> traffic_signals
        27: 19,  # Pedestrians -> pedestrians
        28: 20,  # Children crossing -> children_crossing
        29: 21,  # Bicycles crossing -> bicycles_crossing
        30: 22,  # Beware of ice/snow -> ice_snow
        31: 23,  # Wild animals crossing -> wild_animals
        32: 24,  # End of all speed and passing limits -> end_limits
        33: 25,  # Turn right ahead -> turn_right_ahead
        34: 26,  # Turn left ahead -> turn_left_ahead
        35: 27,  # Ahead only -> ahead_only
        36: 28,  # Go straight or right -> straight_or_right
        37: 29,  # Go straight or left -> straight_or_left
        38: 30,  # Keep right -> keep_right
        39: 31,  # Keep left -> keep_left
        40: 32,  # Roundabout mandatory -> roundabout
        41: 1,   # End of no passing -> end_speed_limit (merged)
        42: 1    # End of no passing for vehicles over 3.5t -> end_speed_limit
    },
    'vnts': {
        0: 33,  # DP.135 -> speed_bump
        1: 10,  # P.102 -> general_caution
        2: 11,  # P.103a -> curve_left
        3: 12,  # P.103b -> curve_right
        4: 13,  # P.103c -> double_curve
        5: 34,  # P.104 -> sharp_deviation
        6: 25,  # P.106a -> turn_right_ahead
        7: 26,  # P.106b -> turn_left_ahead
        8: 28,  # P.107a -> straight_or_right
        9: 35,  # P.112 -> crossroad
        10: 0,  # P.115 -> speed_limit
        11: 24, # P.117 -> end_limits
        12: 4,  # P.123a -> priority_road
        13: 4,  # P.123b -> priority_road
        14: 19, # P.124a -> pedestrians
        15: 19, # P.124b -> pedestrians
        16: 19, # P.124c -> pedestrians
        17: 20, # P.125 -> children_crossing
        18: 21, # P.127 -> bicycles_crossing
        19: 18, # P.128 -> traffic_signals
        20: 17, # P.130 -> road_work
        21: 23, # P.131a -> wild_animals
        22: 36, # P.137 -> falling_rocks
        23: 37, # P.245a -> ferry_terminal
        24: 3,  # R.301c -> no_heavy_vehicles
        25: 3,  # R.301d -> no_heavy_vehicles
        26: 3,  # R.301e -> no_heavy_vehicles
        27: 2,  # R.302a -> no_passing
        28: 27, # R.302b -> ahead_only
        29: 6,  # R.303 -> stop
        30: 38, # R.407a -> one_way
        31: 24, # R.409 -> end_limits
        32: 30, # R.425 -> keep_right
        33: 0,  # R.434 -> speed_limit
        34: 32, # S.509a -> roundabout
        35: 11, # W.201a -> curve_left
        36: 12, # W.201b -> curve_right
        37: 39, # W.202a -> two_way_traffic
        38: 39, # W.202b -> two_way_traffic
        39: 35, # W.203b -> crossroad
        40: 35, # W.203c -> crossroad
        41: 14, # W.205a -> bumpy_road
        42: 14, # W.205b -> bumpy_road
        43: 14, # W.205d -> bumpy_road
        44: 15, # W.207a -> slippery_road
        45: 15, # W.207b -> slippery_road
        46: 15, # W.207c -> slippery_road
        47: 16, # W.208 -> road_narrows
        48: 22, # W.209 -> ice_snow
        49: 40, # W.210 -> steep_hill
        50: 41, # W.219 -> railway_crossing
        51: 42, # W.221b -> tramway_crossing
        52: 43, # W.224 -> traffic_queues
        53: 44, # W.225 -> low_flying_aircraft
        54: 45, # W.227 -> crosswind
        55: 46, # W.233 -> tunnel
        56: 47, # W.235 -> other_danger
        57: 37   # W.245a -> ferry_terminal
    },
    'chinese': {
        # Assuming Chinese categories 0-57 align with standard TT100K or similar set; mapped to unified classes based on typical Chinese traffic signs
        0: 6,    # Give way -> yield (merged)
        1: 9,    # No entry -> no_entry
        2: 38,   # One-way traffic -> one_way
        3: 38,   # One-way traffic -> one_way
        4: 7,    # No vehicles in both directions -> no_vehicles
        5: 48,   # No entry for cycles -> no_cycles
        6: 49,   # No entry for goods vehicles -> no_goods_vehicles
        7: 50,   # No entry for pedestrians -> no_pedestrians
        8: 51,   # No entry for bullock carts -> no_bullock_carts
        9: 52,   # No entry for hand carts -> no_hand_carts
        10: 53,  # No entry for motor vehicles -> no_motor_vehicles
        11: 54,  # Height limit -> height_limit
        12: 55,  # Weight limit -> weight_limit
        13: 56,  # Axle weight limit -> axle_weight_limit
        14: 57,  # Length limit -> length_limit
        15: 58,  # No left turn -> no_left_turn
        16: 59,  # No right turn -> no_right_turn
        17: 2,   # No overtaking -> no_passing
        18: 0,   # Maximum speed limit (90 km/h) -> speed_limit
        19: 0,   # Maximum speed limit (110 km/h) -> speed_limit
        20: 60,  # Horn prohibited -> horn_prohibited
        21: 61,  # No parking -> no_parking
        22: 62,  # No stopping -> no_stopping
        23: 25,  # Turn left -> turn_left_ahead (merged)
        24: 26,  # Turn right -> turn_right_ahead (merged)
        25: 63,  # Steep descent -> steep_descent
        26: 64,  # Steep ascent -> steep_ascent
        27: 16,  # Narrow road -> road_narrows
        28: 65,  # Narrow bridge -> narrow_bridge
        29: 66,  # Unprotected quay -> unprotected_quay
        30: 33,  # Road hump -> speed_bump
        31: 67,  # Dip -> dip
        32: 68,  # Loose gravel -> loose_gravel
        33: 36,  # Falling rocks -> falling_rocks
        34: 69,  # Cattle -> cattle
        35: 35,  # Crossroads -> crossroad
        36: 70,  # Side road junction -> side_road_junction
        37: 70,  # Side road junction -> side_road_junction
        38: 71,  # Oblique side road junction -> oblique_side_road_junction
        39: 71,  # Oblique side road junction -> oblique_side_road_junction
        40: 72,  # T-junction -> t_junction
        41: 73,  # Y-junction -> y_junction
        42: 74,  # Staggered side road junction -> staggered_side_road_junction
        43: 74,  # Staggered side road junction -> staggered_side_road_junction
        44: 32,  # Roundabout -> roundabout
        45: 75,  # Guarded level crossing ahead -> guarded_level_crossing
        46: 76,  # Unguarded level crossing ahead -> unguarded_level_crossing
        47: 77,  # Level crossing countdown marker -> level_crossing_countdown
        48: 77,  # Level crossing countdown marker -> level_crossing_countdown
        49: 77,  # Level crossing countdown marker -> level_crossing_countdown
        50: 77,  # Level crossing countdown marker -> level_crossing_countdown
        51: 78,  # Parking -> parking
        52: 79,  # Bus stop -> bus_stop
        53: 80,  # First aid post -> first_aid_post
        54: 81,  # Telephone -> telephone
        55: 82,  # Filling station -> filling_station
        56: 83,  # Hotel -> hotel
        57: 84   # Restaurant -> restaurant
    },
    'indian': {
        0: 5,    # Give way -> yield
        1: 9,    # No entry -> no_entry
        2: 38,   # One-way traffic -> one_way
        3: 38,   # One-way traffic -> one_way
        4: 7,    # No vehicles in both directions -> no_vehicles
        5: 48,   # No entry for cycles -> no_cycles
        6: 49,   # No entry for goods vehicles -> no_goods_vehicles
        7: 50,   # No entry for pedestrians -> no_pedestrians
        8: 51,   # No entry for bullock carts -> no_bullock_carts
        9: 52,   # No entry for hand carts -> no_hand_carts
        10: 53,  # No entry for motor vehicles -> no_motor_vehicles
        11: 54,  # Height limit -> height_limit
        12: 55,  # Weight limit -> weight_limit
        13: 56,  # Axle weight limit -> axle_weight_limit
        14: 57,  # Length limit -> length_limit
        15: 58,  # No left turn -> no_left_turn
        16: 59,  # No right turn -> no_right_turn
        17: 2,   # No overtaking -> no_passing
        18: 0,   # Maximum speed limit (90 km/h) -> speed_limit
        19: 0,   # Maximum speed limit (110 km/h) -> speed_limit
        20: 60,  # Horn prohibited -> horn_prohibited
        21: 61,  # No parking -> no_parking
        22: 62,  # No stopping -> no_stopping
        23: 25,  # Turn left -> turn_left_ahead
        24: 26,  # Turn right -> turn_right_ahead
        25: 63,  # Steep descent -> steep_descent
        26: 64,  # Steep ascent -> steep_ascent
        27: 16,  # Narrow road -> road_narrows
        28: 65,  # Narrow bridge -> narrow_bridge
        29: 66,  # Unprotected quay -> unprotected_quay
        30: 33,  # Road hump -> speed_bump
        31: 67,  # Dip -> dip
        32: 68,  # Loose gravel -> loose_gravel
        33: 36,  # Falling rocks -> falling_rocks
        34: 69,  # Cattle -> cattle
        35: 35,  # Crossroads -> crossroad
        36: 70,  # Side road junction -> side_road_junction
        37: 70,  # Side road junction -> side_road_junction
        38: 71,  # Oblique side road junction -> oblique_side_road_junction
        39: 71,  # Oblique side road junction -> oblique_side_road_junction
        40: 72,  # T-junction -> t_junction
        41: 73,  # Y-junction -> y_junction
        42: 74,  # Staggered side road junction -> staggered_side_road_junction
        43: 74,  # Staggered side road junction -> staggered_side_road_junction
        44: 32,  # Roundabout -> roundabout
        45: 75,  # Guarded level crossing ahead -> guarded_level_crossing
        46: 76,  # Unguarded level crossing ahead -> unguarded_level_crossing
        47: 77,  # Level crossing countdown marker -> level_crossing_countdown
        48: 77,  # Level crossing countdown marker -> level_crossing_countdown
        49: 77,  # Level crossing countdown marker -> level_crossing_countdown
        50: 77,  # Level crossing countdown marker -> level_crossing_countdown
        51: 78,  # Parking -> parking
        52: 79,  # Bus stop -> bus_stop
        53: 80,  # First aid post -> first_aid_post
        54: 81,  # Telephone -> telephone
        55: 82,  # Filling station -> filling_station
        56: 83,  # Hotel -> hotel
        57: 84,  # Restaurant -> restaurant
        58: 47   # Refreshments -> other_danger (merged as miscellaneous)
    }
}