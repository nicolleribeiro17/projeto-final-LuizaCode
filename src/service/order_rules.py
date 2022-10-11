from typing import List, Optional
from uuid import uuid4
 
from server import order_servers
from models.order import Order, OrderGeneral
 
from service.rules_exception import OtherExceptionRules, RulesException, ExceptionNotFound, OtherCodesExceptions
 
CAMPO_CODE = order_servers.OrderField.CODE
 
# procura o endereço pelo codigo do usuário
async def search_by_code(code: str, throws_exception_if_not_found: bool = False) -> Optional[dict]:
    order = await order_servers.get_by_code(code)
    if not order and throws_exception_if_not_found:
        raise ExceptionNotFound("Usuário não encontrado")
    return order
 
# busca todos
async def search_all() -> List[dict]:
    all = await order_servers.get_all()
    return all
 
 
 
# async def validate_order(order: Order, code_base: Optional[str] = None):
#     is_new_order = code_base is None
     
#     other_order = await order_server.get_by_code(order.code)
#     if (other_order is not None) and (
#         is_new_order or
#         (code_base != other_order[CAMPO_CODE])
#     ):
#         raise OtherExceptionRules("Há outro usuário com este código")
 
 
async def insert_new_order(order: Order) -> OrderGeneral:
    new_order = order.dict()
    new_order[order_servers.OrderField.CODE] = str(uuid4())
    await order_servers.create_new_order(new_order)
    order_geral = OrderGeneral(**new_order)
    return order_geral
 
 
async def remove_by_code(code: str):
    remove = await order_servers.delete_by_code(code)
 
    if not remove:
        raise ExceptionNotFound("Usuário não encontrada")
 
 
async def update_by_code(code: str, order: OrderGeneral):
    await search_by_code(code, True)
 
    if order.code is not None and order.code != code:
        raise OtherCodesExceptions
    # validate_order(order, code)
 
    order_for_database = order.dict()
 
    if order.code is None:
        order_for_database.pop(CAMPO_CODE, None)
 
    await order_servers.update_order_by_code(
        code, order_for_database
    )
 
 
 

