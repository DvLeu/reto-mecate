from app.repositories.externalapi_repo import StackOverflowRepo

class ExternalService:
    def __init__(self, repo: StackOverflowRepo):
        self.repo = repo
        
    async def respondidas_no_respondidas(self):
        items = await self.repo.fetch_questions()
        respondidas = sum(1 for i in items if i.get("is_answered"))
        no_respondidas = len(items) - respondidas
        
        print("Respondidas:", respondidas)
        print("No respondidas:", no_respondidas)
        
        return {
            "respondidas": respondidas,
            "no_respondidas": no_respondidas, 
            "total": len(items)
        }

    async def mayor_reputacion(self):
        items = await self.repo.fetch_questions()
        result = max(items, key=lambda x: x.get("owner", {}).get("reputation", 0))
        
        print("Mayor reputacion:", result.get("owner", {}).get("display_name"))
        print("Puntos:", result.get("owner", {}).get("reputation"))
        
        data = {
            "titulo": result.get("title"),
            "owner": result.get("owner", {}).get("display_name"),
            "reputacion": result.get("owner", {}).get("reputation"),
            "link": result.get("link")
        }
        return data

    async def menor_vistas(self):
        items = await self.repo.fetch_questions()
        result = min(items, key=lambda x: x.get("view_count", float("inf")))
        
        print("Menor vistas:", result.get("view_count"))
        
        data = {
            "titulo": result.get("title"),
            "vistas": result.get("view_count"),
            "link": result.get("link")
        }
        return data

    async def mas_vieja_y_actual(self):
        items = await self.repo.fetch_questions()
        oldest = min(items, key=lambda x: x.get("creation_date", float("inf")))
        newest = max(items, key=lambda x: x.get("creation_date", 0))
        
        print("Mas vieja:", oldest.get("title"))
        print("Mas reciente:", newest.get("title"))
        
        data = {
            "mas_vieja": {
                "titulo": oldest.get("title"),
                "fecha_creacion": oldest.get("creation_date"),
                "link": oldest.get("link")
            },
            "mas_actual": {
                "titulo": newest.get("title"),
                "fecha_creacion": newest.get("creation_date"),
                "link": newest.get("link")
            }
        }
        return data