from abc import ABC, abstractmethod

class ExcelGatewayInterface(ABC):
    @abstractmethod
    def create_excel_file():
        pass