CLI : TODO

사용법

todo + 해야 할 일

flag type

명령어 종류:
1. add
    해야 할 일 추가하는 명령어. flag 없이 사용해도 해야 할 일 추가 가능.
    flag 종류
    --date : 해야 할 일의 날짜 (format: 16_JUN_2001, ...)
    --time : 해야 할 일의 시간 (format: 23_00, 21_45, ...)
        date나 time의 format이 맞지 않을 경우 에러 발생
    
    명령어 사용 예시 : 
    todo add Meeting_with_Dowan_Kim --date 30_JUL_2025 --time 10_30
    todo add Lab_Meeting --time 14:30
    todo add James_River_Tour --date 02_AUG_2025
    todo add Dinner --date 30_JUL_2025 --time 18:00

2. show
    지금까지 저장된 해야 할 일 리스트를 날짜 및 시간 순으로 출력해서 보여주는 명령어
    날짜나 시간이 공란일 경우, 맨 마지막 순으로 밀리고 그들 사이에는 선후관게는 중요치 않다. 

    명령어 사용 예시 :
    todo show

    결과 양식 :
    
    |인덱스|  해야 할 일  | 날짜 | 시간 | 

    결과 예시 : 
    
    | 0 | Meeting_with_Dowan_Kim | 30.JUL.2025 | 10:30 |
    | 1 | Dinner | 30.JUL.2025 | 18:00 |
    | 2 | James_River_Tour | 02.AUG.2025 |  |
    | 3 | Lab_Meeing |  | 14:30 |


3. clear
    지금까지 저장된 모든 해야 할 일 리스트를 삭제.

    명령어 사용 예시 : 
    todo clear

    명령어 실행 후 todo show 실행 결과 :



    기존 todo 리스트가 사라진 것을 확인할 수 있다.

4. delete
    show 명령어를 쳤을 때 나오는 index에 대하여 삭제하고 싶은 todo 항목을 삭제한다. 

    명령어 사용예시 : 
    todo delete 1

    명령어 실행 후 todo show 실행 결과 : 
    | 0 | Meeting_with_Dowan_Kim | 30.JUL.2025 | 10:30 |
    | 1 | James_River_Tour | 02.AUG.2025 |  |
    | 2 | Lab_Meeing |  | 14:30 |

    
    기존의 index 1에 해당하던 Dinner 항목이 삭제된 것을 확인할 수 있다.

5. fix
    show 명령어를 쳤을 때 나오는 index에 대하여 수정하고 싶은 todo item을 선택하여 수정을 실행한다.
    flag 종류
    --date : 입력할 날짜로 기존 날짜를 수정
    --time : 입력할 시간으로 기존 시간을 수정
    두 flag롤 모두 사용할 필요는 없지만, 적어도 하나의 flag는 사용해야 하며, flag 없이 이 명령어를 칠 시, 에러 발생.

    명령어 사용 예시 : 
    todo fix 0 --date 29.JUL.2025 --time 10_00
    명령어 실행 후 todo show 실행 결과 :
    | 0 | Meeting_with_Dowan_Kim | 29.JUL.2025 | 10:00 |
    | 1 | James_River_Tour | 02.AUG.2025 |  |
    | 2 | Lab_Meeing |  | 14:30 |

    명령어 사용 예시 : 
    todo fix 1 : --time 11_00
    명령어 실행 후 todo show 실행 결과 :
    실행 결과 :
    | 0 | Meeting_with_Dowan_Kim | 29.JUL.2025 | 10:00 |
    | 1 | James_River_Tour | 02.AUG.2025 | 11:00 |
    | 2 | Lab_Meeing |  | 14:30 |

    명령어 사용 예시 : 
    todo fix 2 : --date 30.JUL.2025
    명령어 실행 후 todo show 실행 결과 : 
    | 0 | Meeting_with_Dowan_Kim | 29.JUL.2025 | 10:00 |
    | 1 | Lab_Meeing | 30.JUL.2025 | 14:30 |
    | 2 | James_River_Tour | 02.AUG.2025 | 11:00 |

6. mdel
    totext 브랜치와 organize 브랜치가 생성된 이후 시점에서, master 브랜치에서 한 번에 여러 index의 항목들을 delete 할 수 있도록 기능 추가할 예정

    명령어 사용예시 : 
    todo mdel 1 3 4



-----------------------------------------------------메인 기능----------------------------------------------------
    
