def make_sandwich(*ingridients):
    """Summarize ingridients of a sandwich"""
    print("\nPreparing sandwich with:")
    for ingridient in ingridients:
        print(f"- {ingridient.title()}")
    print("Enjoy your sandwich!")

    return make_sandwich