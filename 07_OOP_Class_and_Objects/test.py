def __str__(self):
    return "\n".join(f"Heap {i}: {v} balls"
                     for (i,v) in enumerate(self.listOfNumBalls, start=1))

