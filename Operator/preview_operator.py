import bpy
import os
from .. Functions import functions

class GOVIE_Preview_Operator(bpy.types.Operator):
    bl_idname = "scene.open_web_preview"
    bl_label = "Open in Browser"
    bl_description = "Press export to display preview of exported file"
    
    port = 8000
    url = "https://3dit-tools.s3.eu-central-1.amazonaws.com/StaticGLBViewer/index.html#model=http://127.0.0.1:"+str(port)+"/export.glb"


    @classmethod
    def poll(cls, context):
        file_path = bpy.data.filepath
        project_dir = os.path.dirname(file_path)
        filename = context.scene.export_settings.glb_filename
        glb_path = os.path.join(project_dir,'glb','')
        glb_file = glb_path + filename + ".glb"

        if os.path.exists(glb_file):
            return True
        return False


    def execute(self, context):
        file_path = bpy.data.filepath
        project_dir = os.path.dirname(file_path)
        filename = context.scene.export_settings.glb_filename
        glb_path = os.path.join(project_dir,'glb','')
        glb_file = glb_path + filename + ".glb"

        script_file = os.path.realpath(__file__)
        script_dir = os.path.dirname(script_file)
        server_path = os.path.join(script_dir, '..',"Server\server.py")

        functions.start_server(server_path,glb_file,self.port)
        # run browser
        bpy.ops.wm.url_open(url = self.url)
        return {"FINISHED"}
