import numpy as np
import open3d as o3d

def generate_dna_structure(turns=10, points_per_turn=100):
    theta = np.linspace(0, 2 * np.pi * turns, turns * points_per_turn)
    radius = 0.5
    x1, y1, z1 = radius * np.sin(theta), radius * np.cos(theta), np.linspace(0, turns, len(theta))
    x2, y2, z2 = radius * np.sin(theta + np.pi), radius * np.cos(theta + np.pi), z1

    dna_cloud = o3d.geometry.PointCloud()
    dna_cloud.points = o3d.utility.Vector3dVector(np.vstack([np.column_stack((x1, y1, z1)), np.column_stack((x2, y2, z2))]))

    o3d.visualization.draw_geometries([dna_cloud])

generate_dna_structure()
