import numpy as np
import open3d as o3d

def stretch_dna(factor=1.5):
    theta = np.linspace(0, 4 * np.pi, 100)
    x = np.sin(theta)
    y = np.cos(theta)
    z = np.linspace(0, factor, 100)
    points = np.column_stack([x, y, z])

    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(points)
    o3d.visualization.draw_geometries([cloud])

stretch_dna()
