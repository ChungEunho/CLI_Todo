# stoarge.py는 실제 json 입출력 담당

import json
from pathlib import Path
from .models import TodoItem
from .utils import sort_key

STORAGE_PATH = Path("todo.json")

# JSON 파일에서 TodoItem 리스트 불러오기
def load_items() -> list[TodoItem]:
    if not STORAGE_PATH.exists() or STORAGE_PATH.stat().st_size == 0:
        return []
    with open(STORAGE_PATH, "r") as f:
        data = json.load(f)
    items = [TodoItem.from_dict(d) for d in data]
    return(sorted(items, key=sort_key))

# TodoItem 리스트 전체를 JSON 파일로 저장
def save_items(items: list[TodoItem]):
    with open(STORAGE_PATH, "w") as f:
        json.dump([item.to_dict() for item in items], f, indent = 2)

# 새 항목 추가 (기존 리스트에 append 후 저장)
def add_item(item: TodoItem):
    items = load_items()
    items.append(item)
    save_items(items)
    
# 인덱스에 해당하는 항목 삭제
def delete_item(index: int):
    items = load_items()
    if 0 <= index < len(items):
        del items[index]
        save_items(items)
    else:
        raise IndexError("Invalid index")
    
# 전체 항목 삭제
def clear_items():
    save_items([])

# 인덱스의 항목 수정
def update_item(index: int, date=None, time=None):
    items = load_items()
    if 0 <= index < len(items):
        if date is not None:
            items[index].date = date
        if time is not None:
            items[index].time = time
        save_items(items)
    else:
        raise IndexError("Invalid index")
    
    
