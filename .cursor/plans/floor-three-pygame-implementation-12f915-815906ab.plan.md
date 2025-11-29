<!-- 815906ab-28a9-4532-9179-9c4fd2e2789b 70dea473-329d-4180-89c3-896928f95dbc -->
# Floor Three: Pygame Top-Down Exploration Plan

## Overview

Create `floors/floor_three.py` as a pygame-based top-down exploration game with puzzle elements. The floor will integrate with the existing inventory and save systems, following the same pattern as floors one and two.

## Key Requirements

- Top-down 2D exploration gameplay using pygame
- Puzzle elements integrated into the exploration
- Full integration with inventory system (receive inventory, return updated inventory)
- Save system integration for progress tracking
- Follow existing floor pattern: function takes `inventory` parameter, returns `inventory`
- Add pygame to requirements.txt
- Update main.py to call floor_three after floor_two

## Implementation Details

### 1. Core Structure (`floors/floor_three.py`)

- Function signature: `def floor_three(inventory):`
- Initialize pygame window (recommended: 800x600 or 1024x768)
- Game loop with event handling
- Player sprite/character for top-down movement (WASD or arrow keys)
- Room-based exploration system (multiple rooms to explore)
- Exit condition that returns inventory when floor is complete

### 2. Gameplay Features

- **Player Movement**: Top-down character movement with keyboard controls
- **Room System**: Multiple rooms/areas to explore (similar to text-based floors but visual)
- **Puzzle Elements**: 
- Item-based puzzles (use inventory items to solve)
- Environmental puzzles (push blocks, activate switches, etc.)
- Logic puzzles (sequence solving, pattern matching)
- **Item Collection**: Visual items that can be picked up and added to inventory
- **Visual Feedback**: Clear indication of interactable objects, puzzle solutions

### 3. Integration Points

- **Inventory Integration**: 
- Display current inventory in UI
- Use items from inventory to solve puzzles
- Add new items found in floor three
- Save inventory state using `functions.save`
- **Save System**: 
- Save progress state (puzzles solved, items collected, rooms visited)
- Load saved state on floor entry
- Update save data structure to include floor three progress
- **Stats Display**: Option to view stats (similar to floor_one and floor_two)

### 4. Technical Implementation

- **Dependencies**: Add `pygame` to `requirements.txt`
- **Window Management**: Handle window close events gracefully
- **State Management**: Track puzzle states, room states, collected items
- **Asset Management**: Use simple pygame primitives (rectangles, circles) or load sprites if available
- **Error Handling**: Graceful handling of pygame initialization failures

### 5. File Modifications

- **`floors/floor_three.py`**: New file with complete pygame implementation
- **`main.py`**: 
- Import floor_three: `import floors.floor_three as f3`
- After floor_two: `inventory = f3.floor_three(inventory)`
- Add floor_three option to dev tools menu
- **`requirements.txt`**: Add `pygame` dependency
- **`functions/save.py`**: May need to extend save data structure for floor three state

### 6. Design Considerations

- **Visual Style**: Simple but clear graphics (can use colored rectangles/circles initially)
- **UI Elements**: 
- Inventory display (sidebar or overlay)
- Instructions/controls hint
- Puzzle feedback messages
- **Room Themes**: 3-4 distinct rooms with different puzzle types
- **Progression**: Clear path to completion (all puzzles solved → exit to next floor)

### 7. Puzzle Examples

- **Item Puzzle**: Use specific inventory item on object to unlock door
- **Sequence Puzzle**: Activate switches in correct order
- **Block Puzzle**: Push blocks to create path or activate pressure plates
- **Collection Puzzle**: Find and collect all items in room to unlock exit

## Implementation Steps

1. Add pygame to requirements.txt
2. Create basic pygame window structure in floor_three.py
3. Implement player movement and basic room rendering
4. Add room system with multiple explorable areas
5. Implement puzzle mechanics (start with one puzzle type)
6. Add inventory display and item interaction
7. Integrate save/load system for floor three state
8. Add remaining puzzle types
9. Implement floor completion condition
10. Update main.py to call floor_three
11. Test integration with existing floors

## Notes

- Keep pygame window size reasonable for different screen sizes
- Consider adding a way to exit pygame window and return to text-based floors gracefully
- Ensure pygame doesn't interfere with terminal-based game flow
- May want to add a "skip" option for players who prefer text-based gameplay

### To-dos

- [ ] Set up pygame window, game loop, and basic event handling in floor_three.py
- [ ] Implement player sprite and WASD/arrow key movement with collision detection
- [ ] Create room-based navigation system with multiple rooms and transitions
- [ ] Implement 2-3 puzzle rooms with different puzzle types (item-based, logic, pattern)
- [ ] Add on-screen inventory display and item usage mechanics
- [ ] Integrate save/load system for floor three progress and handle KeyboardInterrupt
- [ ] Update main.py to import and call floor_three after floor_two
- [ ] Add pygame to requirements.txt