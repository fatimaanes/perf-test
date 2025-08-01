import time
import random
import math

# PERFORMANCE TUNING GUIDE:
# To create performance improvements or regression: DECREASE or INCREASE the numbers marked with # TUNE
# Example: change "range(800)" to "range(600)" for improvement or "range(1000)" for regression


class FPSBenchmarks:
    
    def setup(self):
        self.entities = 900  # TUNE
        self.vertices = list(range(self.entities * 3))
        self.transforms = {i: (random.random(), random.random(), random.random()) 
                          for i in range(self.entities)}
        self.visible_entities = [random.randint(0, self.entities-1) for _ in range(800)]  # TUNE

    def time_fps_rendering(self):
        result = []
        for entity_id in self.visible_entities:
            if entity_id in self.transforms:
                x, y, z = self.transforms[entity_id]
                transformed = (x * 1.5, y * 1.2, z * 0.8)
                result.append(transformed)
        return result

    def time_fps_physics(self):
        collisions = []
        for i in range(0, len(self.visible_entities)-1):
            entity1 = self.visible_entities[i] 
            entity2 = self.visible_entities[i+1]
            distance = abs(entity1 - entity2)
            if distance < 5:
                collisions.append((entity1, entity2))
        return collisions

    def time_fps_culling(self):
        visible = []
        for entity_id in range(self.entities):
            if entity_id % 3 == 0:
                visible.append(entity_id)
        return visible

    def time_fps_animation(self):
        animated = []
        for i in range(min(150, len(self.visible_entities))):  # TUNE
            entity_id = self.visible_entities[i]
            for bone in range(20):  # TUNE
                animated.append(entity_id * bone * 0.1)
        return animated


class CPUBenchmarks:
    params = [1000, 5000, 10000]
    param_names = ['entities']

    def setup(self, entities):
        self.ai_agents = [{'pos': (random.random()*100, random.random()*100), 
                          'health': random.randint(50, 100),
                          'target': None} for _ in range(entities)]
        self.physics_objects = [random.random() * 10 for _ in range(entities)]

    def time_cpu_ai_pathfinding(self, entities):
        paths = []
        for agent in self.ai_agents[:min(80, len(self.ai_agents))]:  # TUNE
            start_x, start_y = agent['pos']
            target_x, target_y = 50.0, 50.0
            distance = math.sqrt((target_x - start_x)**2 + (target_y - start_y)**2)
            paths.append(distance)
        return sum(paths)

    def time_cpu_physics_integration(self, entities):
        velocities = []
        for obj_mass in self.physics_objects:
            acceleration = 9.81
            velocity = obj_mass * acceleration * 0.016
            velocities.append(velocity)
        return sum(velocities)

    def time_cpu_audio_processing(self, entities):
        audio_samples = []
        sample_count = min(entities, 2048)  # TUNE
        for i in range(sample_count):
            sample = math.sin(i * 0.1) * math.cos(i * 0.05)
            audio_samples.append(sample)
        return audio_samples

    def time_cpu_network_updates(self, entities):
        updates = []
        for i in range(0, min(entities, 64)):  # TUNE
            update = {'id': i, 'pos': self.ai_agents[i]['pos'], 
                     'health': self.ai_agents[i]['health']}
            updates.append(hash(str(update)))
        return updates


class GPUBenchmarks:
    
    def setup(self):
        self.vertices = [(random.random(), random.random(), random.random()) 
                        for _ in range(4000)]  # TUNE
        self.textures = ['texture_' + str(i) for i in range(200)]
        self.shader_uniforms = {f'uniform_{i}': random.random() for i in range(64)}

    def time_gpu_vertex_processing(self):
        transformed_vertices = []
        for vertex in self.vertices:
            x, y, z = vertex
            transformed = (x * 1.2 + 0.1, y * 0.8 - 0.2, z * 1.5)
            transformed_vertices.append(transformed)
        return transformed_vertices

    def time_gpu_texture_sampling(self):
        samples = []
        for texture in self.textures:
            for u in [0.0, 0.5, 1.0]:
                for v in [0.0, 0.5, 1.0]:
                    sample = hash(texture + str(u) + str(v)) % 256
                    samples.append(sample)
        return samples

    def time_gpu_compute_shaders(self):
        compute_results = []
        workgroup_size = 64  # TUNE
        for group in range(len(self.vertices) // workgroup_size):
            group_result = 0
            for i in range(workgroup_size):
                idx = group * workgroup_size + i
                if idx < len(self.vertices):
                    x, y, z = self.vertices[idx]
                    group_result += x * y * z
            compute_results.append(group_result)
        return compute_results

    def time_gpu_fragment_processing(self):
        fragments = []
        screen_width, screen_height = 1920, 1080
        sample_count = 800  # TUNE
        for i in range(sample_count):
            x = (i % screen_width) / screen_width
            y = (i // screen_width) / screen_height
            combined_light = math.sin(x * math.pi) * math.cos(y * math.pi * 2)
            fragments.append(combined_light)
        return fragments


class MemoryBenchmarks:
    
    def mem_texture_cache(self):
        return [0] * (4096 * 4096 * 4)

    def mem_vertex_buffers(self):
        return [0.0] * (10000 * 12)

    def mem_audio_buffers(self):
        return [0] * (48000 * 2 * 4)

    def mem_entity_components(self):
        return [{'transform': (0, 0, 0), 'health': 100, 'ai_state': 'idle'} 
                for _ in range(1000)]

    def mem_shader_cache(self):
        return {'vertex_shader_' + str(i): [random.randint(0, 255) for _ in range(1024)]
                for i in range(50)}


class PerformanceMetrics:
    
    def track_target_fps(self):
        frame_times = [16.67, 15.2, 18.1, 16.9, 15.8]
        avg_frame_time = sum(frame_times) / len(frame_times)
        target_fps = 1000.0 / avg_frame_time
        return round(target_fps)

    def track_memory_usage_mb(self):
        texture_mem = 256
        vertex_mem = 64
        audio_mem = 32
        script_mem = 128
        return texture_mem + vertex_mem + audio_mem + script_mem

    def track_draw_calls(self):
        terrain_calls = 12
        character_calls = 24
        effect_calls = 18
        ui_calls = 6
        return terrain_calls + character_calls + effect_calls + ui_calls

    def track_active_entities(self):
        players = 4
        npcs = 28
        projectiles = 16
        particles = 156
        return players + npcs + projectiles + particles

    def track_gpu_utilization(self):
        vertex_load = 65
        fragment_load = 78
        compute_load = 45
        avg_utilization = (vertex_load + fragment_load + compute_load) // 3
        return avg_utilization

    track_target_fps.unit = "fps"
    track_memory_usage_mb.unit = "MB"
    track_draw_calls.unit = "calls"
    track_active_entities.unit = "entities" 
    track_gpu_utilization.unit = "percent"
