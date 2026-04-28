# logic/styling_engine.py

def get_aesthetic_advice(aesthetic):
    """Returns key takeaways and style items based on user input."""
    
    aesthetics_db = {
        "y2k": {
            "takeaways": "Focus on tech-optimism, futuristic fabrics, and playful silhouettes.",
            "items": ["Baby tees", "Low-rise denim", "Butterfly clips", "Velour tracksuits"],
            "hair": "High pigtails, spiky buns, or face-framing braids."
        },
        "ethereal": {
            "takeaways": "Focus on light-weight fabrics, soft colors, and a dream-like flow.",
            "items": ["Chiffon skirts", "Sheer tops", "Pearl jewelry", "Corset tops"],
            "hair": "Loose waves, micro-braids with ribbons, or soft 'cloud' curls."
        },
        "alt": {
            "takeaways": "Focus on subverting traditional silhouettes and using heavy textures.",
            "items": ["Oversized hoodies", "Chunky boots", "Safety pin accessories", "Distressed knits"],
            "hair": "Shag cuts, blunt bangs, or high-contrast colors."
        }
    }

    # Normalize input to lowercase to avoid errors
    choice = aesthetic.lower()

    if choice in aesthetics_db:
        data = aesthetics_db[choice]
        print(f"--- ELUNÏA ANALYSIS: {choice.upper()} ---")
        print(f"KEY VIBE: {data['takeaways']}")
        print(f"MUST-HAVE ITEMS: {', '.join(data['items'])}")
        print(f"HAIR INSPO: {data['hair']}")
    else:
        print("Aesthetic not found. Try 'Y2K', 'Ethereal', or 'Alt'.")

# Test the engine
user_input = input("Enter your desired aesthetic: ")
get_aesthetic_advice(user_input)
