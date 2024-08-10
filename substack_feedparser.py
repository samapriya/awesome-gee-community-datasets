import feedparser


def get_blog_info(feed_url, num_entries=20):
    """
    Fetches blog titles and links from an RSS feed.
    Args:
        feed_url: The URL of the RSS feed.
        num_entries: The number of entries to extract (default: 5).
    Returns:
        A list of dictionaries, each containing the title and link for a blog entry.
    """
    feed = feedparser.parse(feed_url)
    entries = []
    for entry in feed.entries[:num_entries]:
        entry_data = {
            "title": entry.title,
            "link": entry.link
        }
        entries.append(entry_data)
    return entries

def update_markdown_file(filename, blog_info, start_marker, end_marker):
    """
    Updates a markdown file with blog info between specified markers.
    Args:
        filename: The name of the markdown file.
        blog_info: A list of dictionaries containing blog title and link.
        start_marker: The marker indicating the start of the section to update.
        end_marker: The marker indicating the end of the section to update.
    """
    with open(filename, 'r',encoding='utf-8') as f:
        file_content = f.read()

    start_index = file_content.find(start_marker) + len(start_marker)
    end_index = file_content.find(end_marker)

    new_content = ""
    for entry in blog_info:
        new_content += f"* [{entry['title']}]({entry['link']})\n"

    updated_content = file_content[:start_index] + "\n" + new_content + file_content[end_index:]

    with open(filename, 'w',encoding='utf-8') as f:
        f.write(updated_content)
    print(f"Updated {filename} successfully!")

# Example usage
feed_url = "https://datacommons.substack.com/feed"
blog_info = get_blog_info(feed_url)

filename = "docs/substack_blogs.md"  # Replace with your markdown filename
start_marker = "<!-- START_MARKER -->"
end_marker = "<!-- END_MARKER -->"

update_markdown_file(filename, blog_info, start_marker, end_marker)


