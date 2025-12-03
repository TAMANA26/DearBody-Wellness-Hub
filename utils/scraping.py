import requests
from bs4 import BeautifulSoup

def get_trending_recipes():
    url = "https://www.allrecipes.com/recipes/"
    recipes = []

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.content, 'html.parser')

        cards = soup.select("a.card__titleLink.manual-link-behavior")[:5]
        for card in cards:
            title = card.get_text(strip=True)
            link = card['href']
            recipes.append({'title': title, 'link': link})
    except Exception as e:
        recipes.append({'title': 'Error fetching recipes', 'link': str(e)})

    return recipes


# 2. Transformation Stories
def get_transformation_stories():
    url = "https://www.healthline.com/health/fitness-nutrition/weight-loss-success-stories"
    stories = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        articles = soup.find_all('a', class_='css-13v1u5b')[:5]

        for article in articles:
            title = article.get_text(strip=True)
            link = "https://www.healthline.com" + article.get('href')
            stories.append({'title': title, 'link': link})
    except Exception as e:
        stories.append({'title': 'Error fetching stories', 'link': str(e)})

    return stories

# 3. Healthy Food Swaps
def get_food_swaps():
    url = "https://www.eatthis.com/healthy-food-swaps/"
    swaps = []

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        bullets = soup.find_all('li')[:5]

        for b in bullets:
            text = b.get_text(strip=True)
            if "Instead of" in text or "Try" in text:
                swaps.append(text)
    except Exception as e:
        swaps.append(f"Error fetching food swaps: {str(e)}")

    return swaps
