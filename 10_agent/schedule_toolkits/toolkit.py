from typing import List
from langchain_core.tools import BaseTool
from langchain.agents.agent_toolkits.base import BaseToolkit

from .tools import AddTodoTool, ViewTodoTool

class ScheduleToolkit(BaseToolkit):
    """Schedule management tool kit"""
    def get_tools(self) -> List[BaseTool]:
        return [AddTodoTool(), ViewTodoTool()]