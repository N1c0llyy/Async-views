import time
import asyncio
from time import sleep

import httpx
from django.http import JsonResponse, HttpResponse


def api(request):
    time.sleep(1)
    payload = {"message": "Hello, World!"}

    if "task_id" in request.GET:
        payload["task_id"] = request.GET["task_id"]

    return JsonResponse(payload)


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"[ASYNC LOOP] {num}")

    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r.status_code)


def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(f"[SYNC LOOP] {num}")

    r = httpx.get("https://httpbin.org/")
    print(r.status_code)


async def async_view(request):
    await http_call_async()
    return HttpResponse("Non-blocking HTTP request")


def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")


async def contador_view(request):
    for i in range(1, 6):
        print(f"Contador: {i}")
        await asyncio.sleep(1)

    return HttpResponse("Contador assíncrono finalizado!")


async def enviar_tarefa():
    for i in range(1, 6):
        await asyncio.sleep(1)
        print(f"Enviando tarefa... etapa {i}")

    print("Tarefa enviada com sucesso!")


async def enviar_view(request):
    await enviar_tarefa()
    return HttpResponse("Envio iniciado.")