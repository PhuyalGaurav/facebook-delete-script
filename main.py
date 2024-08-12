import requests
import time
import environs

# Load environment variables
env = environs.Env()
env.read_env()

# Constants
USER_ACCESS_TOKEN = env.str('USER_ACCESS_TOKEN')
PAGE_ID = env.str('PAGE_ID')
GRAPH_API_URL = 'https://graph.facebook.com/v20.0'


def get_page_access_token(user_access_token, page_id):
    url = f"{GRAPH_API_URL}/me/accounts"
    params = {
        'access_token': user_access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        pages = response.json().get('data', [])
        
        for page in pages:
            if page['id'] == page_id:
                return page['access_token']
        
    else:
        print(f"Error fetching page access token: {response.status_code}")
        print(f"Response: {response.json()}")
    return None

def get_posts(page_id, access_token):
    url = f"{GRAPH_API_URL}/{page_id}/posts"
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        posts = response.json().get('data', [])
        print(f"Fetched {len(posts)} posts.")
        return posts
    else:
        print(f"Error fetching posts: {response.status_code}")
        print(f"Response: {response.json()}")
        return []

def delete_post(post_id, access_token):
    url = f"{GRAPH_API_URL}/{post_id}"
    params = {
        'access_token': access_token
    }
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        print(f"Post {post_id} deleted successfully.")
        return True
    else:
        error_message = response.json().get('error', {}).get('message', '')
        if "This post wasn't created by the application" in error_message:
            print(f"Skipping post {post_id}: {error_message}")
            return True  # Skip this post and continue
        else:
            print(f"Error deleting post {post_id}: {response.status_code}")
            print(f"Response: {response.json()}")
            return False

def main():
    page_access_token = get_page_access_token(USER_ACCESS_TOKEN, PAGE_ID)
    if page_access_token:
        posts = get_posts(PAGE_ID, page_access_token)
        for post in posts:
            success = delete_post(post['id'], page_access_token)
            if not success:
                print(f"Failed to delete post {post['id']}. Retrying...")
                time.sleep(5)  # Wait before retrying
                success = delete_post(post['id'], page_access_token)
                if not success:
                    print(f"Failed to delete post {post['id']} after retrying. Skipping...")
    else:
        print("Failed to retrieve page access token.")

if __name__ == "__main__":
    while True:
        main()