import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def find_unfollowers():
    followers_path = os.path.join(BASE_DIR, "connections/followers_and_following", "followers_1.json")
    following_path = os.path.join(BASE_DIR, "connections/followers_and_following", "following.json")

    with open(followers_path, 'r') as f:
        f_data = json.load(f)
    with open(following_path, 'r') as g:
        g_data = json.load(g)

    # Unwrap the 'relationships_following' wrapper
    following_list = g_data.get('relationships_following', []) if isinstance(g_data, dict) else g_data

    def extract_names(data_list):
        names = set()
        for entry in data_list:
            try:
                # 1. Access the inner list
                inner = entry['string_list_data'][0]
                
                # 2. Try 'value' first (your snippet), fallback to 'href' if missing
                name = inner.get('value')
                
                # 3. If 'value' is empty, clean up the 'href' (e.g., https://instagram.com)
                if not name and 'href' in inner:
                    name = inner['href'].split('/')[-1]
                
                if name:
                    names.add(name)
            except (KeyError, IndexError, TypeError):
                continue
        return names

    followers = extract_names(f_data)
    following = extract_names(following_list)

    unfollowers = following - followers

    print(f"Followers: {len(followers)} | Following: {len(following)}")
    print(f"\nNot following you back ({len(unfollowers)}):")
    for user in sorted(unfollowers):
        print(user)

find_unfollowers()