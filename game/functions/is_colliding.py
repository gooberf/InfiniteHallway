def top(walls, player):
    for i in walls:
        return (
    player.colliderect(i)
    and player.top <= i.top
        )

def bottom(walls, player):
    for i in walls:
        return (
    player.colliderect(i)
    and player.bottom <= i.bottom
        )

def left(walls, player):
    for i in walls:
        return (
    player.colliderect(i)
    and player.left <= i.left
        )
    
def right(walls, player):
    for i in walls:
        return (
    player.colliderect(i)
    and player.right <= i.right
        )

