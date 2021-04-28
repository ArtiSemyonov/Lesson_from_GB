# Я не до конца понял данное задание, поэтому поискав в интеренете и почитав темы по декораторам,
# нашел и переписал немного код под исключение valueError , но разбираться еще прилично в этой теме
# Так же, я использовал модуль functools для работы с декораторами и почитал о нем.
import functools


def validate_summary(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        data = func(*args, **kwargs)
        if len(data["summary"]) > 30:
            raise ValueError("Ваше резюме превышает 30 символов.")
        return data

    return wrapper


@validate_summary
def short_summary():
    return {"summary": "Этот резюме короткое"}


@validate_summary
def long_summary():
    return {"summary": "Это резюме слишком длинное оно превышает лимит символов."}


print(short_summary())
print(long_summary())
