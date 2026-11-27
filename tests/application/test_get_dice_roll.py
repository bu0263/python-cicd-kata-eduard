from app.application.get_dice_roll import get_dice_roll


def test_result_is_a_valid_dice_value() -> None:
    for _ in range(100):
        result = get_dice_roll()
        assert isinstance(result, int)
        assert result in {10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
