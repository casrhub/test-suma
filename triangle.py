def calculate_triangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a triangle.
    
    Args:
        base (float): The base of the triangle
        height (float): The height of the triangle
        
    Returns:
        float: The area of the triangle
        
    Raises:
        ValueError: If base or height is negative or if base is zero
    """
    if base <= 0:
        raise ValueError("Base must be greater than zero")
    if height < 0:
        raise ValueError("Height cannot be negative")
        
    return (base * height) / 2 