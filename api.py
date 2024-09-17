# # import instaloader

# # # Function to get followers and following list
# # def get_followers_and_following(username):
# #     # Create an instance of Instaloader
# #     L = instaloader.Instaloader()

# #     # Log in (required to access followers and following lists)
# #     print("Logging in...")
# #     L.login(input("Enter your Instagram username: "), input("Enter your password: "))

# #     # Get the profile
# #     profile = instaloader.Profile.from_username(L.context, username)

# #     # Fetch followers
# #     print(f"Fetching followers of {username}...")
# #     followers = set([follower.username for follower in profile.get_followers()])
# #     print(f"Found {len(followers)} followers.")

# #     # Fetch following
# #     print(f"Fetching accounts followed by {username}...")
# #     following = set([followee.username for followee in profile.get_followees()])
# #     print(f"Found {len(following)} accounts followed.")

# #     # Output the lists
# #     with open(f'{username}_followers.txt', 'w') as f:
# #         for follower in followers:
# #             f.write(f"{follower}\n")
# #     with open(f'{username}_following.txt', 'w') as f:
# #         for followee in following:
# #             f.write(f"{followee}\n")

# #     print(f"Followers and following lists saved to {username}_followers.txt and {username}_following.txt.")

# # # Placeholder function for Direct Messages (Instagram API restrictions)
# # # def get_direct_messages():
# # #     print("\nDirect Messages functionality is not available in Instaloader.")
# # #     print("Direct message fetching requires access to Instagram's private API, which is not supported by Instaloader.")

# # # Function to get direct messages (DMs)
# # def get_direct_messages(api):
# #     try:
# #         threads = api.direct_v2_inbox()
# #         print("\nDirect Messages:")
# #         for thread in threads['inbox']['threads']:
# #             print(f"Message Thread with {', '.join([user['username'] for user in thread['users']])}:")
# #             for message in thread['items']:
# #                 print(f"- {message['text'] if 'text' in message else 'No Text'}")
# #     except Exception as e:
# #         print(f"Failed to fetch direct messages: {e}")

# # if __name__ == "__main__":
# #     # Input the target Instagram username
# #     target_username = input("Enter the target Instagram username: ")

# #     # Fetch followers and followings
# #     get_followers_and_following(target_username)

# #     # Placeholder for direct message fetching
# #     get_direct_messages()





# # from instagram_private_api import Client, ClientCompatPatch
# # import uuid

# # # Function to log in to Instagram and get API client
# # def login_to_instagram(username, password):
# #     try:
# #         # Log in to Instagram
# #         api = Client(username, password)
# #         print(f"Successfully logged in as {username}")
# #         return api
# #     except Exception as e:
# #         print(f"Login failed: {e}")
# #         return None

# # # Function to get followers and followings list
# # def get_followers_and_following(api, username):
# #     try:
# #         # Fetch user info to get user_id
# #         user_info = api.username_info(username)
# #         user_id = user_info['user']['pk']

# #         # Generate rank_token
# #         rank_token = Client.generate_uuid()

# #         # Fetch followers
# #         print(f"Fetching followers of {username}...")
# #         followers = api.user_followers(user_id, rank_token=rank_token)['users']
# #         follower_usernames = [follower['username'] for follower in followers]
# #         print(f"Found {len(follower_usernames)} followers.")
        
# #         # Fetch followings
# #         print(f"Fetching accounts followed by {username}...")
# #         following = api.user_following(user_id, rank_token=rank_token)['users']
# #         following_usernames = [followee['username'] for followee in following]
# #         print(f"Found {len(following_usernames)} accounts followed.")

# #         # Save followers and following to files
# #         with open(f'{username}_followers.txt', 'w') as f:
# #             for follower in follower_usernames:
# #                 f.write(f"{follower}\n")
# #         with open(f'{username}_following.txt', 'w') as f:
# #             for followee in following_usernames:
# #                 f.write(f"{followee}\n")

# #         print(f"Followers and following lists saved to {username}_followers.txt and {username}_following.txt.")
# #     except Exception as e:
# #         print(f"Error fetching followers/following: {e}")

# # # Function to get direct messages (DMs)
# # def get_direct_messages(api):
# #     try:
# #         # Fetch direct message inbox
# #         threads = api.direct_v2_inbox()['inbox']['threads']
# #         print("\nDirect Messages:")
# #         for thread in threads:
# #             users_in_thread = ', '.join([user['username'] for user in thread['users']])
# #             print(f"Message Thread with {users_in_thread}:")
# #             for message in thread['items']:
# #                 message_text = message['text'] if 'text' in message else 'No Text'
# #                 print(f"- {message_text}")
# #     except Exception as e:
# #         print(f"Failed to fetch direct messages: {e}")

# # if __name__ == "__main__":
# #     # Input your Instagram credentials
# #     username = input("Enter your Instagram username: ")
# #     password = input("Enter your Instagram password: ")

# #     # Log in and get API client
# #     api = login_to_instagram(username, password)

# #     if api:
# #         # Input the target username (can be the same as your login username)
# #         target_username = input("Enter the target Instagram username: ")

# #         # Fetch followers and followings
# #         get_followers_and_following(api, target_username)

# #         # Fetch direct messages
# #         get_direct_messages(api)









# ################finalllllll cccoooodddeeeeeeeeee##########
# from instagram_private_api import Client, ClientCompatPatch
# import uuid

# # Function to log in to Instagram and get API client
# def login_to_instagram(username, password):
#     try:
#         # Log in to Instagram
#         api = Client(username, password)
#         print(f"Successfully logged in as {username}")
#         return api
#     except Exception as e:
#         print(f"Login failed: {e}")
#         return None

# # Function to get followers and followings list and save to a file
# def get_followers_and_following(api, username, output_file):
#     try:
#         # Fetch user info to get user_id
#         user_info = api.username_info(username)
#         user_id = user_info['user']['pk']

#         # Generate rank_token
#         rank_token = Client.generate_uuid()

#         # Fetch followers
#         print(f"Fetching followers of {username}...")
#         followers = api.user_followers(user_id, rank_token=rank_token)['users']
#         follower_usernames = [follower['username'] for follower in followers]
#         print(f"Found {len(follower_usernames)} followers.")

#         # Fetch followings
#         print(f"Fetching accounts followed by {username}...")
#         following = api.user_following(user_id, rank_token=rank_token)['users']
#         following_usernames = [followee['username'] for followee in following]
#         print(f"Found {len(following_usernames)} accounts followed.")

#         # Write followers and following to file
#         with open(output_file, 'a') as f:
#             f.write(f"\nFollowers of {username}:\n")
#             for follower in follower_usernames:
#                 f.write(f"{follower}\n")
            
#             f.write(f"\nAccounts followed by {username}:\n")
#             for followee in following_usernames:
#                 f.write(f"{followee}\n")

#         print(f"Followers and following lists saved to {output_file}.")
#     except Exception as e:
#         print(f"Error fetching followers/following: {e}")

# # Function to get direct messages (DMs) and save to a file
# def get_direct_messages(api, output_file):
#     try:
#         # Fetch direct message inbox
#         threads = api.direct_v2_inbox()['inbox']['threads']
#         print("\nDirect Messages:")
#         with open(output_file, 'a') as f:
#             f.write("\nDirect Messages:\n")
#             for thread in threads:
#                 users_in_thread = ', '.join([user['username'] for user in thread['users']])
#                 f.write(f"Message Thread with {users_in_thread}:\n")
#                 print(f"Message Thread with {users_in_thread}:")
#                 for message in thread['items']:
#                     message_text = message['text'] if 'text' in message else 'No Text'
#                     f.write(f"- {message_text}\n")
#                     print(f"- {message_text}")
#         print(f"Direct messages saved to {output_file}.")
#     except Exception as e:
#         print(f"Failed to fetch direct messages: {e}")

# if __name__ == "__main__":
#     # Input your Instagram credentials
#     username = input("Enter your Instagram username: ")
#     password = input("Enter your Instagram password: ")

#     # Log in and get API client
#     api = login_to_instagram(username, password)

#     if api:
#         # Input the target username (can be the same as your login username)
#         target_username = input("Enter the target Instagram username: ")

#         # Define output file
#         output_file = f'{target_username}_instagram_data.txt'

#         # Fetch followers and followings and save to file
#         get_followers_and_following(api, target_username, output_file)

#         # Fetch direct messages and save to file
#         get_direct_messages(api, output_file)

#         print(f"All data saved to {output_file}.")













import os
from instagram_private_api import Client
from datetime import datetime

# Helper function to format the timestamp
def format_timestamp(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

# Function to log in to Instagram and get API client
def login_to_instagram(username, password):
    try:
        # Log in to Instagram
        api = Client(username, password)
        print(f"Successfully logged in as {username}")
        return api
    except Exception as e:
        print(f"Login failed: {e}")
        return None

# Function to get followers and followings list and save to a file
def get_followers_and_following(api, username, output_file):
    try:
        # Fetch user info to get user_id
        user_info = api.username_info(username)
        user_id = user_info['user']['pk']

        # Generate rank_token
        rank_token = Client.generate_uuid()

        # Fetch followers
        print(f"Fetching followers of {username}...")
        followers = api.user_followers(user_id, rank_token=rank_token)['users']
        follower_usernames = [follower['username'] for follower in followers]
        print(f"Found {len(follower_usernames)} followers.")

        # Fetch followings
        print(f"Fetching accounts followed by {username}...")
        following = api.user_following(user_id, rank_token=rank_token)['users']
        following_usernames = [followee['username'] for followee in following]
        print(f"Found {len(following_usernames)} accounts followed.")

        # Write followers and following to file
        with open(output_file, 'a') as f:
            f.write(f"\nFollowers of {username}:\n")
            for follower in follower_usernames:
                f.write(f"{follower}\n")
            
            f.write(f"\nAccounts followed by {username}:\n")
            for followee in following_usernames:
                f.write(f"{followee}\n")

        print(f"Followers and following lists saved to {output_file}.")
    except Exception as e:
        print(f"Error fetching followers/following: {e}")

# Function to get direct messages (DMs) with timelines and save to a file
def get_direct_messages(api, output_file):
    try:
        # Fetch direct message inbox
        threads = api.direct_v2_inbox()['inbox']['threads']
        print("\nDirect Messages:")
        with open(output_file, 'a') as f:
            f.write("\nDirect Messages:\n")
            for thread in threads:
                users_in_thread = ', '.join([user['username'] for user in thread['users']])
                f.write(f"Message Thread with {users_in_thread}:\n")
                print(f"Message Thread with {users_in_thread}:")
                for message in thread['items']:
                    message_text = message['text'] if 'text' in message else 'No Text'
                    timestamp = format_timestamp(message['timestamp'] / 1000000)  # Convert from microseconds
                    f.write(f"- [{timestamp}] {message_text}\n")
                    print(f"- [{timestamp}] {message_text}")
        print(f"Direct messages with timeline saved to {output_file}.")
    except Exception as e:
        print(f"Failed to fetch direct messages: {e}")

# New function to download posts and save media files
def download_post_media(api, post, download_dir):
    try:
        media_type = post['media_type']  # Check if it's an image, video, or album
        post_code = post['code']  # Unique identifier for post
        post_url = f"https://www.instagram.com/p/{post_code}/"

        # Download based on media type
        if media_type == 1:  # Image
            image_url = post['image_versions2']['candidates'][0]['url']
            filename = f"{post_code}.jpg"
        elif media_type == 2:  # Video
            video_url = post['video_versions'][0]['url']
            filename = f"{post_code}.mp4"
        elif media_type == 8:  # Album (carousel of images/videos)
            filename = f"{post_code}_album"
            # Process each media in the carousel
            for i, item in enumerate(post['carousel_media']):
                if item['media_type'] == 1:  # Image
                    image_url = item['image_versions2']['candidates'][0]['url']
                    media_filename = f"{post_code}_image_{i + 1}.jpg"
                    media_path = os.path.join(download_dir, media_filename)
                    save_media(image_url, media_path)
                elif item['media_type'] == 2:  # Video
                    video_url = item['video_versions'][0]['url']
                    media_filename = f"{post_code}_video_{i + 1}.mp4"
                    media_path = os.path.join(download_dir, media_filename)
                    save_media(video_url, media_path)
            return filename

        # Save media
        media_path = os.path.join(download_dir, filename)
        media_url = image_url if media_type == 1 else video_url
        save_media(media_url, media_path)

        return filename
    except Exception as e:
        print(f"Error downloading media: {e}")
        return None

# Helper function to save media file
def save_media(url, path):
    try:
        response = api.session.get(url)
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded media to {path}")
    except Exception as e:
        print(f"Error saving media: {e}")

# New function to get posts, download media, and save all info in the output file
def get_posts_and_comments(api, username, output_file, download_dir):
    try:
        # Fetch user info to get user_id
        user_info = api.username_info(username)
        user_id = user_info['user']['pk']

        # Fetch posts (media)
        print(f"Fetching posts for {username}...")
        posts = api.user_feed(user_id)['items']

        # Write posts, comments, and post links to the file with timeline
        with open(output_file, 'a') as f:
            f.write(f"\nPosts by {username}:\n")
            for post in posts:
                caption = post['caption']['text'] if post['caption'] else 'No Caption'
                timestamp = format_timestamp(post['taken_at'])
                post_code = post['code']  # Unique identifier for post
                post_url = f"https://www.instagram.com/p/{post_code}/"  # Construct post URL
                
                # Download media
                downloaded_filename = download_post_media(api, post, download_dir)

                # Write post details to file
                f.write(f"\nPost ID: {post['id']}\n")
                f.write(f"Posted on: {timestamp}\n")
                f.write(f"Post URL: {post_url}\n")
                f.write(f"Caption: {caption}\n")
                f.write(f"Downloaded Media: {downloaded_filename}\n")
                print(f"\nPost ID: {post['id']}")
                print(f"Posted on: {timestamp}")
                print(f"Post URL: {post_url}")
                print(f"Caption: {caption}")
                print(f"Downloaded Media: {downloaded_filename}")

                # Fetch comments for each post
                comments = api.media_n_comments(post['id'], n=10)  # Fetch top 10 comments
                f.write("Comments:\n")
                for comment in comments:
                    comment_text = comment['text']
                    commenter = comment['user']['username']
                    comment_timestamp = format_timestamp(comment['created_at'])
                    f.write(f"- [{comment_timestamp}] {commenter}: {comment_text}\n")
                    print(f"- [{comment_timestamp}] {commenter}: {comment_text}")

        print(f"Posts, comments, and post links with timelines saved to {output_file}.")
    except Exception as e:
        print(f"Error fetching posts and comments: {e}")

if __name__ == "__main__":
    # Input your Instagram credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # Log in and get API client
    api = login_to_instagram(username, password)

    if api:
        # Input the target username (can be the same as your login username)
        target_username = input("Enter the target Instagram username: ")

        # Define output file
        output_file = f'{target_username}_instagram_data.txt'
        download_dir = f'{target_username}_media'  # Directory to save downloaded media

        # Create media download directory if it doesn't exist
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)

        # Fetch followers and followings and save to file
        get_followers_and_following(api, target_username, output_file)

        # Fetch direct messages and save to file
        get_direct_messages(api, output_file)

        # Fetch posts and comments, download media, and save everything to file
        get_posts_and_comments(api, target_username, output_file, download_dir)

        print(f"All data and media saved to {output_file} and {download_dir}.")
