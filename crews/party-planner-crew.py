import warnings
warnings.filterwarnings("ignore")

from crewai import Agent, Task, Crew
from crewai_tools import ScrapeWebsiteTool, \
                         SerperDevTool
from pydantic import BaseModel


# Define a Pydantic model for venue details 
# (demonstrating Output as Pydantic)
class VenueDetails(BaseModel):
    name: str
    address: str
    capacity: int
    booking_status: str

search_tool = SerperDevTool()
scrape_tool = ScrapeWebsiteTool()


party_planner_agent = Agent(
    role="Party Planner",
    goal="Plan a fun and memorable party for a special occasion.",
    backstory=(
        "As a Party Planner, you are responsible for creating unforgettable experiences for your clients."
        "From selecting the perfect venue to organizing the entertainment and catering, your attention to detail"
        "and creativity are key to ensuring that every event is a success."
    ),
    verbose=True
)

marketing_agent = Agent(
    role="Marketing Agent",
    goal="Promote the party to attract guests and create buzz around the event.",
    backstory=(
        "As a Marketing Agent, you play a crucial role in generating excitement and interest in the party."
        "From creating engaging social media posts to reaching out to influencers and media outlets, your marketing"
        "skills are essential in attracting guests and ensuring the success of the event."
    ),
    verbose=True
)

logistics_manager_agent = Agent(
    role="Logistics Manager",
    goal="Coordinate the logistics of the party to ensure everything runs smoothly.",
    backstory=(
        "As a Logistics Manager, you play a crucial role in ensuring that all the moving parts of an event come together seamlessly."
        "From managing vendors and coordinating schedules to overseeing setup and breakdown, your organizational skills"
        "and attention to detail are essential to the success of the party."
    ),
    allow_delegation=True,
    verbose=True
)

find_place_task = Task(
    name="Find a Place",
    description=(
        "Find a place that is available on the date {date} to host the party in the city of {city}."
        "the vibe of the place should be {vibe}."
    ),
    expected_output="The name of the place and the address.",
    tools=[search_tool, scrape_tool],
    human_input=True,
    agent=party_planner_agent,
    output_json=VenueDetails,
    output_file="venue_details.json",
)

create_social_media_post_task = Task(
    name="Create Social Media Post",
    description=(
        "Create {number_of_posts} social media post(s) to promote the party."
        "The post should be engaging and creative."
    ),
    expected_output=(
        "A social media post with engaging content that will be later shared"
        "The content shouldn't be offensive or inappropriate."
    ),
    # tools=[search_tool, scrape_tool],
    agent=marketing_agent,
    async_execution=True,
    output_file="social_media_posts.md"
)

party_planner_crew = Crew(
    name="Party Planner Crew",
    agents=[party_planner_agent, marketing_agent],
    tasks=[find_place_task, create_social_media_post_task]
)

party_planner_crew.kickoff(inputs={
    "date": "2025-06-01",
    "city": "Amsterdam",
    "vibe": "Eletronic party for a group of friends",
    "number_of_posts": 3
})