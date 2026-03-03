import os
import pickle
from dotenv import load_dotenv
from agentmanager import CloudAgentManager
from LLMGraphTransformer import LLMGraphTransformer
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

cloud_agent_manager = CloudAgentManager()

PROVIDER = "groq"
API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "openai/gpt-oss-20b"

llm = cloud_agent_manager.prepare_llm(PROVIDER, API_KEY, MODEL_NAME)

llm_transformer = LLMGraphTransformer(llm=llm)

text = """It all began in Mumbai, where dreams, traffic, and romantic misunderstandings
flowed with equal intensity.
Aarav, an aspiring indie filmmaker with permanently messy hair, was secretly in
love with Meera, a bubbly radio jockey who narrated her life like it was a daily
soap. Meera, however, had eyes only for Kabir — a charming startup founder who
quoted poetry on LinkedIn and thought heartbreak was a “phase.”
Kabir, unfortunately, was head over sneakers for Riya, a fiercely independent
fashion buyer who dressed like every day was Fashion Week. Riya, in turn, was
hopelessly crushing on Dev, a shy travel blogger who communicated mostly through
drone shots and long captions.
And Dev?
Dev had fallen hard for Aarav after Aarav once helped him carry camera equipment
up four flights of stairs during a blackout.
Thus was born the Love Pentagon:
Aarav → Meera → Kabir → Riya → Dev → Aarav.
Round and round it went.
Adding spice to this emotional masala were their friends:
Priya, Meera’s brutally honest roommate; Sameer, Kabir’s gym-obsessed bestie;
Neha, Riya’s sarcastic colleague; and Uncle Joshi, Aarav’s landlord who believed
every problem could be solved with ginger tea.
Things escalated when the whole group traveled to Jaipur for Riya’s cousin’s
wedding. Between palaces, pastel lehengas, and accidental slow dances under
fairy lights, everyone almost confessed their feelings — but always to the wrong
person.
Aarav tried to tell Meera how he felt, but she was busy helping Kabir rehearse a
romantic proposal… meant for Riya.
Riya practiced her “I like you” speech in the mirror, only to deliver it
nervously to Dev — who thought she was talking about her new suitcase.
Meanwhile, Dev filmed a sunset vlog dedicated to Aarav but accidentally tagged
Meera.
Priya watched this chaos unfold and declared, “I’ve seen less complicated plots
in daily soaps.”
The emotional pressure cooker finally exploded during a spontaneous trip to Goa,
organized by Sameer because, in his words, “Bro, beaches heal everything.”
Cue montages: scooter rides, coconut water confessions, late-night karaoke, and
a dramatic rain sequence where everyone blurted out their true feelings on the
beach.
There were tears. There was sand in inappropriate places. Uncle Joshi somehow
appeared with homemade pakoras.
After much confusion, laughter, and one accidental group hug, clarity emerged:
Meera realized Aarav had always been her safest place.
Kabir admitted he admired Riya but genuinely connected with Neha’s dry humor.
Riya discovered Dev’s quiet sensitivity was exactly what she needed.
Dev, relieved, happily accepted Riya’s hand — and promised to film their first
date in cinematic slow motion.
And Aarav?
Aarav finally got Meera.
Sameer remained single but victorious over a seafood platter.
They returned to Mumbai with sunburns, new couples, and one legendary group chat
named “Pentagon Se Hexagon Tak.”
Because in true Bollywood fashion, love didn’t arrive neatly — it danced in
late, tripped over feelings, and left everyone better than it found them.
"""

splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50
    )
chunks = splitter.split_text(text)
document = [Document(page_content=c) for c in chunks]

graph_document = llm_transformer.convert_to_graph_documents(document)

with open("full_graph.pkl", "wb") as f:
    pickle.dump(graph_document, f)

print(graph_document)