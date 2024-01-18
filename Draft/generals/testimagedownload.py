import os
import requests
from googlesearch import search

def get_image_urls(query, num_results=3):
    try:
        results = list(search(query, stop=num_results, pause=2))
        return results
    except StopIteration:
        return []

def download_images(dubai_wharf_tower_3, image_urls, save_folder):
    os.makedirs(save_folder, exist_ok=True)

    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url)
            response.raise_for_status()
            with open(os.path.join(save_folder, f'{dubai_wharf_tower_3}_{i+1}.jpg'), 'wb') as f:
                f.write(response.content)
        except requests.exceptions.RequestException as e:
            print(f"Error downloading image {i+1} for {dubai_wharf_tower_3}: {e}")

def main():
    building_names = ['dubai wharf tower 3', 'another building name', 'and so on']
    save_folder = r'C:\Users\Phyo\OneDrive - Skyloov Property Portal\Skyloov-Phyo\Master_Data\Admin_Portal_Documents\Building Pictures'

    for dubai_wharf_tower_3 in building_names:
        query = f'{dubai_wharf_tower_3} skyscraper site:wikipedia.org'
        image_urls = get_image_urls(query)
        download_images(dubai_wharf_tower_3, image_urls, save_folder)

if __name__ == "__main__":
    main()
