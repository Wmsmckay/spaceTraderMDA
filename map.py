import requests
import matplotlib.pyplot as plt


url = 'https://api.spacetraders.io/v2/systems'
bearer_token = 'YOUR_BEARER_TOKEN'

headers = {
    "Authorization": f"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGlmaWVyIjoiQlVUVF9NVU5DSEVSIiwidmVyc2lvbiI6InYyIiwicmVzZXRfZGF0ZSI6IjIwMjMtMDYtMDMiLCJpYXQiOjE2ODYwNjY0MjEsInN1YiI6ImFnZW50LXRva2VuIn0.j0zC32St4fFN3ZmeQ8x9u6z3tJZzrRpa1Pak1UNKyn3OZ5HX0NeTzkWm_YqZD8P3JO7xU_ML9iwYatiu0xU-EYkaki5L0dIv3jjzOQ0xXQ_KFXA_ZUgw6t2nwEETEqbiFj3AY4FnfFTtCVyDSuwwF1T6Lvw_g0zjXTH5qhJkUSdcS6ivxp0NGksKLsoG6pGm32OqQbCEGDe-tKr4BXmoMOE3Cp_w6XbTCzr821rG7ripRq_cQHwbP23u5Ih60MbTzubXCuN4pp382ZNW-rOAwpaNrTCGo8oVADHH2XfLcDcDU-VIJjXSh8OpN-wDAzCcUblZSFYQ0Mle-3Fq-oAw1A",
}


def get_data():
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            return response_data
        else:
            print(f"Request failed with status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def open_star_map(name):
    # Open a new map for the clicked star (implement your logic here)
    print(f"Opening map for {name}")

def display_universe(data):
    x_values = []
    y_values = []
    names = []
    sizes = []
    colors = []
    hover_texts = []
    possible_colors = ['red', 'blue', 'yellow', 'white', 'orange']

    for i in data:
        x = i['x']
        y = i['y']
        name = i['symbol']
        point_type = (i['type']).lower()
        size = 110  # Default size
        color = 'black'  # Default color

        if 'young' in point_type:
            size = 70
            color = 'lightblue'
        elif 'dwarf' in point_type:
            size = 90
            color = 'blue'
        elif 'neutron' in point_type:
            size = 190
            color = 'white'  # Multi-colored

        if point_type.split('_')[0] in possible_colors:
            color = point_type.split('_')[0]

        x_values.append(x)
        y_values.append(y)
        names.append(name)
        sizes.append(size)
        colors.append(color)
        hover_texts.append(f"Name: {name}\nType: {point_type.replace('_', ' ').title()}")

    def on_hover(event):
        vis = annot.get_visible()
        if event.inaxes is not None:
            cont, ind = scatter.contains(event)
            if cont:
                point_index = ind["ind"][0]
                x = x_values[point_index]
                y = y_values[point_index]
                text = hover_texts[point_index]

                # Calculate the position of the annotation box
                x_offset = 10
                y_offset = 10

                if x > ax.get_xlim()[1] - 50:  # Check if going off the right side
                    x_offset = -90
                if y > ax.get_ylim()[1] - 50:  # Check if going off the top side
                    y_offset = -40

                annot.xy = (x, y)
                annot.set_text(text)
                annot.set_visible(True)
                annot.set_position((x_offset, y_offset))
                fig.canvas.draw()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw()

    def on_click(event):
        if event.inaxes is not None:
            x_click = event.xdata
            y_click = event.ydata
            distances = [(x - x_click) ** 2 + (y - y_click) ** 2 for x, y in zip(x_values, y_values)]
            index = distances.index(min(distances))
            star_name = names[index]
            open_star_map(star_name)

    fig, ax = plt.subplots()

    scatter = ax.scatter(x_values, y_values, s=sizes, c=colors, edgecolor='black')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Space Traders Universe')

    annot = ax.annotate("", xy=(0, 0), xytext=(10, 10), textcoords="offset points",
                        bbox=dict(boxstyle='round, pad=0.5', fc='yellow', alpha=0.8),
                        arrowprops=dict(arrowstyle="->"))

    fig.canvas.mpl_connect('motion_notify_event', on_hover)
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()


json_data = get_data()
if json_data:
    display_universe(json_data['data'])