# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-312-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


from .object import object

class Context(object):
    # no doc
    def append_path(self, *args, **kwargs): # real signature unknown
        pass

    def arc(self, *args, **kwargs): # real signature unknown
        pass

    def arc_negative(self, *args, **kwargs): # real signature unknown
        pass

    def clip(self, *args, **kwargs): # real signature unknown
        pass

    def clip_extents(self, *args, **kwargs): # real signature unknown
        pass

    def clip_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def close_path(self, *args, **kwargs): # real signature unknown
        pass

    def copy_clip_rectangle_list(self, *args, **kwargs): # real signature unknown
        pass

    def copy_page(self, *args, **kwargs): # real signature unknown
        pass

    def copy_path(self, *args, **kwargs): # real signature unknown
        pass

    def copy_path_flat(self, *args, **kwargs): # real signature unknown
        pass

    def curve_to(self, *args, **kwargs): # real signature unknown
        pass

    def device_to_user(self, *args, **kwargs): # real signature unknown
        pass

    def device_to_user_distance(self, *args, **kwargs): # real signature unknown
        pass

    def fill(self, *args, **kwargs): # real signature unknown
        pass

    def fill_extents(self, *args, **kwargs): # real signature unknown
        pass

    def fill_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def font_extents(self, *args, **kwargs): # real signature unknown
        pass

    def get_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_point(self, *args, **kwargs): # real signature unknown
        pass

    def get_dash(self, *args, **kwargs): # real signature unknown
        pass

    def get_dash_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_fill_rule(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_target(self, *args, **kwargs): # real signature unknown
        pass

    def get_hairline(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_cap(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_join(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def get_miter_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_operator(self, *args, **kwargs): # real signature unknown
        pass

    def get_scaled_font(self, *args, **kwargs): # real signature unknown
        pass

    def get_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_target(self, *args, **kwargs): # real signature unknown
        pass

    def get_tolerance(self, *args, **kwargs): # real signature unknown
        pass

    def glyph_extents(self, *args, **kwargs): # real signature unknown
        pass

    def glyph_path(self, *args, **kwargs): # real signature unknown
        pass

    def has_current_point(self, *args, **kwargs): # real signature unknown
        pass

    def identity_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def in_clip(self, *args, **kwargs): # real signature unknown
        pass

    def in_fill(self, *args, **kwargs): # real signature unknown
        pass

    def in_stroke(self, *args, **kwargs): # real signature unknown
        pass

    def line_to(self, *args, **kwargs): # real signature unknown
        pass

    def mask(self, *args, **kwargs): # real signature unknown
        pass

    def mask_surface(self, *args, **kwargs): # real signature unknown
        pass

    def move_to(self, *args, **kwargs): # real signature unknown
        pass

    def new_path(self, *args, **kwargs): # real signature unknown
        pass

    def new_sub_path(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def paint_with_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def path_extents(self, *args, **kwargs): # real signature unknown
        pass

    def pop_group(self, *args, **kwargs): # real signature unknown
        pass

    def pop_group_to_source(self, *args, **kwargs): # real signature unknown
        pass

    def push_group(self, *args, **kwargs): # real signature unknown
        pass

    def push_group_with_content(self, *args, **kwargs): # real signature unknown
        pass

    def rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def rel_curve_to(self, *args, **kwargs): # real signature unknown
        pass

    def rel_line_to(self, *args, **kwargs): # real signature unknown
        pass

    def rel_move_to(self, *args, **kwargs): # real signature unknown
        pass

    def reset_clip(self, *args, **kwargs): # real signature unknown
        pass

    def restore(self, *args, **kwargs): # real signature unknown
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def select_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def set_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def set_dash(self, *args, **kwargs): # real signature unknown
        pass

    def set_fill_rule(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_hairline(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_cap(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_join(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def set_miter_limit(self, *args, **kwargs): # real signature unknown
        pass

    def set_operator(self, *args, **kwargs): # real signature unknown
        pass

    def set_scaled_font(self, *args, **kwargs): # real signature unknown
        pass

    def set_source(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_rgb(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_rgba(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_surface(self, *args, **kwargs): # real signature unknown
        pass

    def set_tolerance(self, *args, **kwargs): # real signature unknown
        pass

    def show_glyphs(self, *args, **kwargs): # real signature unknown
        pass

    def show_page(self, *args, **kwargs): # real signature unknown
        pass

    def show_text(self, *args, **kwargs): # real signature unknown
        pass

    def show_text_glyphs(self, *args, **kwargs): # real signature unknown
        pass

    def stroke(self, *args, **kwargs): # real signature unknown
        pass

    def stroke_extents(self, *args, **kwargs): # real signature unknown
        pass

    def stroke_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def tag_begin(self, *args, **kwargs): # real signature unknown
        pass

    def tag_end(self, *args, **kwargs): # real signature unknown
        pass

    def text_extents(self, *args, **kwargs): # real signature unknown
        pass

    def text_path(self, *args, **kwargs): # real signature unknown
        pass

    def transform(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def user_to_device(self, *args, **kwargs): # real signature unknown
        pass

    def user_to_device_distance(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass


