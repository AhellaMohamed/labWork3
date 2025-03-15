from user_manager import save_topic, add_search_history, view_saved_topics, view_search_history
from news_retriever import fetch_news
from summarizer import summarize_article

def main():
    while True:
        print("\nWelcome to the News Summarization App!")
        print("\nOptions:")
        print("1. Search for news")
        print("2. View saved topics")
        print("3. View search history")
        print("4. Exit")
        
        choice = input("Enter choice: ").strip()

        if choice == "1":
            topic = input("Enter news topic: ").strip()
            add_search_history(topic)  # Save to search history
            articles = fetch_news(topic)

            if not articles:
                print("No articles found.")
            else:
                print("\nFetched Articles:")
                for i, article in enumerate(articles, start=1):
                    print(f"\nArticle {i}: {article['title']}")
                    print(f"URL: {article['url']}")

                    summary_type = input("\nSummarization options:\n1. Brief (1-2 sentences)\n2. Detailed (paragraph)\nChoose summary type (1/2): ").strip()
                    summary = summarize_article(article["content"], summary_type)

                    print("\nSummary:")
                    print(summary)

                # Ask the user if they want to save the topic
                save_choice = input("\nWould you like to save this topic for future reference? (yes/no): ").strip().lower()
                if save_choice == "yes":
                    save_topic(topic)
                    print(f"Topic '{topic}' has been saved.")

        elif choice == "2":
            topics = view_saved_topics()
            if topics:
                print("\nSaved Topics:")
                for topic in topics:
                    print(f"- {topic}")
            else:
                print("No saved topics.")

        elif choice == "3":
            history = view_search_history()
            if history:
                print("\nSearch History:")
                for h in history:
                    print(f"- {h}")
            else:
                print("No search history.")

        elif choice == "4":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        input("\nPress Enter to return to the main menu...")  # Ensures smooth navigation

if __name__ == "__main__":
    main()

