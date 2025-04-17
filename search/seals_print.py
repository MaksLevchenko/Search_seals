def seals_print(seals_count: int) -> str:
    """По числу нерп возвращает слово 'нерпа' с правильным окончанием"""

    if 11 <= seals_count % 100 <= 14:
        return "нерп"
    elif seals_count % 10 == 1:
        return "нерпа"
    elif 2 <= seals_count % 10 <= 4:
        return "нерпы"
    else:
        return "нерп"
