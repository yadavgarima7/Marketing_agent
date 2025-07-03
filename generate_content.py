import json
from dotenv import load_dotenv
from agent import qa_chain

load_dotenv()

# Load brand voice
with open("brand_profile.txt") as f:
    brand_voice = f.read()

# Load competitor (Recess) posts
with open("posts/hello_recess.json") as f:
    recess_data = json.load(f)
    competitor_posts = "\n".join([post["caption"] for post in recess_data if post.get("caption")])

# Load content themes with descriptions
with open("themes.txt") as f:
    themes = [line.strip() for line in f if line.strip()]
theme_prompt = "\n".join([f"{i+1}. {theme}" for i, theme in enumerate(themes)])

# Compose query
query = f"""
You are a content strategist for PlanO — a platform helping parents discover and manage kids’ activity classes.

Use this brand voice:
{brand_voice}

Analyze these recent posts from a competitor (Recess). Identify patterns, tone, and hooks:
{competitor_posts}

Now, generate {len(themes)} Instagram post ideas for PlanO — each one must align with a different content theme:
{theme_prompt}

For each post, include:
- Hook (first line on the image)
- Caption (1–2 sentences)
- Strong CTA
- Relevant hashtags for Greater Seattle area parents
- Suggested image concept (what kind of image would pair with this caption?)

Be creative and avoid repeating phrases or formats.
"""

# Run query
response = qa_chain.invoke({"query": query})
output_text = response["result"]

# Print and save output
print("🪄 PlanO Content Ideas:\n")
print(output_text)

with open("generated_posts.txt", "w") as f:
    f.write(output_text)

print("✅ Content saved to generated_posts.txt")