from fastapi import APIRouter
from src.controllers.cats import CatsController
from src.core.logger import get_logger
from src.schemas.cats import CatSchema, CatUpdateSchema


router = APIRouter()
logger = get_logger(__name__)


@router.get("", response_model=list[CatSchema])
async def get_cats():
    res = await CatsController.get_all_cats()
    return res


@router.get("/{cat_id}", response_model=CatSchema | None)
async def get_cat_by_id(cat_id: int):
    res = await CatsController.get_cat_by_id(cat_id=cat_id)
    return res


@router.post("", response_model=CatSchema)
async def create_cat(cat: CatSchema):
    res = await CatsController.create_cat(data=cat.model_dump())
    return res


@router.patch("/{cat_id}", response_model=CatSchema)
async def update_cat(cat_id: int, data: CatUpdateSchema):
    res = await CatsController.update_cat_by_id(
        cat_id=cat_id, data=data.model_dump(exclude_unset=True)
    )
    return res
