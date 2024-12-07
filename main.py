import subprocess
import json

def get_video_links(channel_url):
    try:
        # Run yt-dlp to fetch video metadata
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "-J", channel_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        data = json.loads(result.stdout)
        
        # Extract video URLs
        video_urls = [f"https://www.youtube.com/watch?v={entry['id']}" for entry in data['entries']]
        return video_urls
    except Exception as e:
        print(f"Error fetching video links: {e}")
        return []

# Get channel URL from the user
channel_name_or_url = input("Enter the YouTube channel name or URL: ").strip()

# Append the /videos endpoint if only the channel name is provided
if "youtube.com" not in channel_name_or_url:
    channel_url = f"https://www.youtube.com/c/{channel_name_or_url}/videos"
else:
    channel_url = channel_name_or_url

print(f"Fetching videos from: {channel_url}")
video_links = get_video_links(channel_url)

# Print the video links
print("\nVideo Links:")
for link in video_links:
    print(link)

# Save to a file
save_file = input("Enter the file name to save links (e.g., video_links.txt): ").strip()
with open(save_file, "w") as file:
    file.write("\n".join(video_links))
print(f"Links saved to {save_file}")
