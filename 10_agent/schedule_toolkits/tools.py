from typing import List, Type
from langchain_core.tools import BaseTool  
from pydantic import BaseModel, Field

# 0. 스케쥴 목록
schedule: List['TodoItem'] = []

# 0-1 스케쥴 스키마
class TodoItem(BaseModel):
    item: str = Field(description='schedule element')
    status: bool = Field(default=False, description='schedule status(True or False)')

# 1 스케쥴 등록 도구
class AddTodoTool(BaseTool):
    name: str = 'add_todo'
    description: str = 'Add an item to the schedule'
    args_schema: Type[BaseModel] = TodoItem
    
    def _run(self, item: str) -> str:
        schedule.append(TodoItem(item=item, status=False))
        return f'Added {item} to schedule'

# 2 스케쥴 확인 도구 설정
class ViewTodoTool(BaseTool):
    name: str = 'view_todos'
    description: str = 'View the schedules'
    
    def _run(self):
        
        if not schedule:
            return 'The schedule is empty'
        
        todo_schedules = '\n'.join(
            f"- {todo.item}" for todo in schedule if not todo.status
        )
    
        return f'Todo Schedule(Not Completed): {todo_schedules}'
    
# TODO
class CompleteTodoTool(BaseTool):
    name: str = 'complete_todo'
    description: str = 'Complete an item from the schedule'
    
    def _run(self):
        
        if not schedule:
            return 'The schedule is empty'
        
        all_schedules = '\n'.join(schedule)
    
        return f'Schedule: {all_schedules}'
    
# TODO
class DeleteTodoTool(BaseTool):
    name: str = 'delete_todo'
    description: str = 'Delete an item from the schedule'
    
    def _run(self):
        
        if not schedule:
            return 'The schedule is empty'
        
        all_schedules = '\n'.join(schedule)
    
        return f'Schedule: {all_schedules}'