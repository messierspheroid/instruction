# # # this line will tell the console that age is only an int
# # age: int
# # name: str
# # height: float
# # is_human: bool
# # # warning that age here is a "string"
# # age = "twelve"
#
# # type hints: preemptively reports a TypeError
#
# def police_check(age: int) -> bool:
#     if age > 18:
#         can_drive = True
#     else:
#         can_drive = False
#     return can_drive
#
#
# # type hint is highlighted below
# if police_check("twelve"):
#     print("You may pass")
# else:
#     print("Pay a fine.")
#
# print(police_check(19))
