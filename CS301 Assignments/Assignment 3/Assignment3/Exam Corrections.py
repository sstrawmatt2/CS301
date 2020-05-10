def search(self, item):
    # Linear time
    current_node = self.get_start()
    time_limit = self.get_global_size()
    while time_limit > 0:
        if current_node.getData() == item:
            return True
        else:
            current_node = current_node.get_next_node()
            time_limit -= 1
    return False


def searcher(self, item_searching_for):
    current_node = self.get_start()
