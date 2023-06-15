from manim import *
import numpy as np

class Project1(ThreeDScene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = ThreeDAxes(x_range=(-2,8),
                          y_range=(-4,4),
                          z_range=(-4,4))
        axes.set_color(BLACK)
        R = 2
        theta = - PI / 3
        self.set_camera_orientation(phi=85 * DEGREES, theta=-75 * DEGREES)
        # cylinder = Cylinder(radius = R, height = 2, direction = X_AXIS, v_range = [1, 5], show_ends = False, resolution=(24,24))
        line_top = axes.plot_parametric_curve(
            lambda t: np.array([t, 0, R]),
            t_range = [-2, 8],
            color = BLACK
        )
        line_bot = axes.plot_parametric_curve(
            lambda t: np.array([t, 0, -R]),
            t_range = [-2, 8],
            color = BLACK
        )
        line_hori = axes.plot_parametric_curve(
            lambda t: np.array([R, t, 0]),
            t_range = [-4, 4],
            color = BLACK
        )
        circle = axes.plot_parametric_curve(
            lambda t: np.array([R, R*np.sin(t), R*np.cos(t)]),
            t_range = [-PI, PI],
            color = BLACK
        )
        Rx = R - 3
        arrow_R = Arrow3D(start=np.array([Rx, 0, 0]),
                          end=np.array([Rx, (R+0.3)*np.sin(theta), (R+0.3)*np.cos(theta)]),
                          color = BLACK)
        arrow_r = Arrow3D(start=np.array([Rx, (R+1)*np.sin(theta), (R+1)*np.cos(theta)]),
                          end=np.array([Rx, (R+2)*np.sin(theta), (R+2)*np.cos(theta)]),
                          color = BLACK)
        arrow_Theta = Arrow3D(start=np.array([0, 0, 0]),
                              end=np.array([2, 2, 2]),
                              color = BLACK)
        arrow_theta_hat = Arrow3D(start=np.array([Rx, (R+0.3)*np.sin(theta), (R+0.3)*np.cos(theta)]),
                              end=np.array([Rx, (R+0.3)*np.sin(theta) + np.sin(PI/2 - theta), (R+0.3)*np.cos(theta) - np.cos(PI/2 - theta)]),
                              color = BLACK)
        arrow_i = Arrow3D(start=np.array([Rx, 0, 0]),
                          end=np.array([Rx+1,0,0]),
                          color = BLACK)
        self.add(axes, line_top, line_bot, circle, arrow_R, arrow_r, arrow_i, line_hori, arrow_theta_hat)