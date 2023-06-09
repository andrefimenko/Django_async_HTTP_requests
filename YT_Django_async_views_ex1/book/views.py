import asyncio
import time

import aiohttp
import requests
from django.shortcuts import render


# def example(request):
#
#     starting_time = time.time()
#
#     pokemon_data = []
#
#     for num in range(1, 101):
#         url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#         res = requests.get(url)
#         pokemon = res.json()
#         pokemon_data.append(pokemon["name"])
#
#     count = len(pokemon_data)
#     total_time = time.time() - starting_time
#
#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )

# async def example(request):
#
#     starting_time = time.time()
#
#     pokemon_data = []
#
#     async with aiohttp.ClientSession() as session:
#         for num in range(1, 101):
#             pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{num}"
#             async with session.get(pokemon_url) as res:
#                 pokemon = await res.json()
#                 pokemon_data.append(pokemon["name"])
#
#     count = len(pokemon_data)
#     total_time = time.time() - starting_time
#
#     return render(
#         request,
#         "index.html",
#         {"data": pokemon_data, "count": count, "time": total_time},
#     )




async def example(request):

    starting_time = time.time()

    pokemon_data = []

    count = len(pokemon_data)
    total_time = time.time() - starting_time

    return render(
        request,
        "index.html",
        {"data": pokemon_data, "count": count, "time": total_time},
    )

# async def example(request):
#     async with aiohttp.ClientSession() as session:
#         async with session.get("https://pokeapi.co/api/v2/pokemon/1") as res:
#             data = await res.json()
#             print(data)
#
#     return render(
#         request,
#         "index.html",
#         {"data": data},
#     )