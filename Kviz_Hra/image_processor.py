"""
Image processing utilities for Kviz_Hra
"""

import os
from PIL import Image
import config


def load_image(image_path: str) -> Image.Image:
    """
    Load an image from file.
    Raises FileNotFoundError if image doesn't exist.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = Image.open(image_path)
    # Convert to RGB if necessary (remove alpha channel)
    if img.mode in ('RGBA', 'LA', 'P'):
        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
        rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
        return rgb_img
    return img.convert('RGB')


def resize_image(img: Image.Image, size: tuple = config.IMAGE_SIZE) -> Image.Image:
    """Resize image to specified size"""
    return img.resize(size, Image.Resampling.LANCZOS)


def get_grid_cells(img: Image.Image, grid_size: int = config.GRID_SIZE) -> list:
    """
    Divide image into grid cells.
    Returns list of 16 PIL Image objects (for 4x4 grid)
    """
    cells = []
    cell_width = img.width // grid_size
    cell_height = img.height // grid_size
    
    for row in range(grid_size):
        for col in range(grid_size):
            left = col * cell_width
            top = row * cell_height
            right = left + cell_width
            bottom = top + cell_height
            
            cell = img.crop((left, top, right, bottom))
            cells.append(cell)
    
    return cells


def create_pixelated_image(img: Image.Image, pixel_size: int = 15) -> Image.Image:
    """
    Create a fully pixelated version of the image.
    Used to show the hidden state of the image grid.
    """
    # Reduce image size for pixelation effect
    small = img.resize(
        (img.width // pixel_size, img.height // pixel_size),
        Image.Resampling.BILINEAR
    )
    # Scale back up to original size
    pixelated = small.resize(img.size, Image.Resampling.NEAREST)
    return pixelated


def create_grid_preview(
    img: Image.Image,
    revealed_cells: list,
    grid_size: int = config.GRID_SIZE,
    pixel_size: int = 15
) -> Image.Image:
    """
    Create an image showing the game grid with some cells revealed.
    
    Args:
        img: The full image
        revealed_cells: List of cell indices that should be revealed (0-15)
        grid_size: Size of grid (default 4 for 4x4)
        pixel_size: Pixelation level for hidden cells
    
    Returns:
        PIL Image with revealed and hidden cells
    """
    # Get original cells
    cells = get_grid_cells(img, grid_size)
    
    # Create pixelated version for hidden cells
    pixelated_cells = get_grid_cells(create_pixelated_image(img, pixel_size), grid_size)
    
    # Create new image
    cell_width = img.width // grid_size
    cell_height = img.height // grid_size
    result = Image.new('RGB', img.size)
    
    # Place cells
    cell_index = 0
    for row in range(grid_size):
        for col in range(grid_size):
            if cell_index in revealed_cells:
                # Use original cell
                cell = cells[cell_index]
            else:
                # Use pixelated cell
                cell = pixelated_cells[cell_index]
            
            left = col * cell_width
            top = row * cell_height
            result.paste(cell, (left, top))
            cell_index += 1
    
    return result


def darken_cell(cell: Image.Image, darkness: float = 0.6) -> Image.Image:
    """
    Darken an image cell for the "hidden" state.
    darkness: 0.0 (fully visible) to 1.0 (fully black)
    """
    # Convert to RGBA for transparency
    cell = cell.convert('RGBA')
    overlay = Image.new('RGBA', cell.size, (0, 0, 0, int(255 * darkness)))
    return Image.alpha_composite(cell, overlay).convert('RGB')


def create_button_image(
    cell: Image.Image,
    revealed: bool = False,
    hover: bool = False,
    size: tuple = (config.CELL_SIZE, config.CELL_SIZE)
) -> Image.Image:
    """
    Create an image for a grid button.
    Shows either pixelated (hidden) or original (revealed).
    """
    cell = cell.resize(size, Image.Resampling.LANCZOS)
    
    if not revealed:
        # Create pixelated effect for hidden cells
        small = cell.resize(
            (size[0] // 3, size[1] // 3),
            Image.Resampling.BILINEAR
        )
        cell = small.resize(size, Image.Resampling.NEAREST)
        
        if hover:
            # Slightly brighten on hover
            cell = Image.blend(cell, Image.new('RGB', cell.size, (100, 100, 100)), 0.3)
    
    return cell


def save_image(img: Image.Image, path: str) -> bool:
    """Save image to file"""
    try:
        img.save(path)
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False
