"""Social Media Manager - undirected graph (adjacency list) implementation.

ITDPA2-44 Data Structures and Algorithms in Python - Question 2.
"""
import networkx as nx
import matplotlib.pyplot as plt


# Connection Manager Class
class ConnectionManager:
    def __init__(self):
        self.network = {}

    def add_user(self, username):
        if username not in self.network:
            self.network[username] = []
            print(f"User '{username}' added.\n")
        else:
            print("User already exists.\n")

    def add_connection(self, user1, user2):
        if user1 in self.network and user2 in self.network:
            if user2 not in self.network[user1]:
                self.network[user1].append(user2)
                self.network[user2].append(user1)
                print(f"Connection added between {user1} and {user2}.\n")
            else:
                print("Connection already exists.\n")
        else:
            print("One or both users do not exist.\n")

    def view_all_users(self):
        print("\nAll Users:")
        for user in self.network:
            print("-", user)
        print()

    def view_all_connections(self):
        print("\nAll Connections:")
        for user, connections in self.network.items():
            print(f"{user}: {', '.join(connections) if connections else 'No connections'}")
        print()

    def display_graph(self):
        G = nx.Graph()
        for user, connections in self.network.items():
            for conn in connections:
                G.add_edge(user, conn)
        nx.draw(G, with_labels=True, node_color="skyblue", node_size=2000, font_size=10, font_weight="bold")
        plt.title("Social Network Graph")
        plt.show()

# Main Menu
def main():
    manager = ConnectionManager()

    while True:
        print("===== Social Media Manager Menu =====")
        print("1. Add User")
        print("2. Add Connection")
        print("3. View All Users")
        print("4. View All Connections")
        print("5. Display Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user = input("Enter username: ")
            manager.add_user(user)
        elif choice == "2":
            u1 = input("Enter first username: ")
            u2 = input("Enter second username: ")
            manager.add_connection(u1, u2)
        elif choice == "3":
            manager.view_all_users()
        elif choice == "4":
            manager.view_all_connections()
        elif choice == "5":
            manager.display_graph()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
