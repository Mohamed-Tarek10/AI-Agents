# Created by: Mohamed Tarek

import json
import os
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from pydantic import BaseModel, ValidationError
from agents import Agent, Runner, WebSearchTool, ModelSettings
import asyncio

_ = load_dotenv(find_dotenv())

client = OpenAI(api_key = os.dot_env.get("OPEN_AI_API_KEY"))


class TravelOutput(BaseModel):
    destination : str
    duration : str
    summary : str


travel_agent = Agent(
    name = "Travel Agent",
    model = "gpt-5",
    instruction =( 
        "your are a friendly and knowledgeable travel planner," 
    " you will help the use to plan their next trip," 
    " you will provide a destination, duration and a summary of the trip, and create a brief summary about the trip.Always return your response as a JSON response, matching to this structure:" 
    '{ \"destination\": \"<destination>\", \"duration\": \"<duration>\", \"summary\": \"<summary>\" }'
    ), 
output_type = TravelOutput,
model_swttings = ModelSettings(
    reseoning = {"effort": "medium"}, # keep the reasoning medium to take enough time to think and provide the answer.
    extra_body = {"text": {"verbosity": "low"}} # Keep response short, concise and to the point
    )
)



 # ----print function helper-----
def print_field(data):
    if isinstance(data, str):
        try:
            data = TravelOutput(**json.loads(data))
        except (json.JSONDecodeError, ValidationError) as e:
            print("Raw Output: ", data)
            return
    print(f"Destination: {data.dstination}")
    print(f"Duration: {data.Duration}")
    print(f"Summary: {data.summary}")



async def main():
    try:
        result = await Runner.run(travel_agent, "Plan a week trip to Egypt under $1000")
        print_field(result.final_output)
    except Exception as e:
        print("Error:", e)


    
if __name__ == "__main__":
    asyncio.run(main())