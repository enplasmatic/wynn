import pygame
import os
import sys

# Main window and basic drawing/events class
class Gradbit:
    def __init__(self, arg):
        pygame.init()
        # Unpack window dimensions and title
        length, width, title = arg
        self.length = length
        self.width = width  # Fixed assignment to self.width
        self.screen = pygame.display.set_mode((length, width))
        self.title = title
        pygame.display.set_caption(title)
        self._running = True
        self.eventList = []
    
    def bitFlags(self, flags):
        # Reinitialize the screen with additional flags (e.g., RESIZABLE)
        self.screen = pygame.display.set_mode((self.length, self.width), flags)
        
    def rename(self, title: str):
        self.title = title
        pygame.display.set_caption(title)
        
    def construct(self, FPS: int):
        # Setup clock for framerate control
        self.fps = FPS
        self.clock = pygame.time.Clock()
        
    def quit(self):
        self._running = False
        pygame.quit()
        sys.exit()
        
    def erase(self, color):
        # Fill the screen with a solid color (commonly used to clear the screen)
        self.screen.fill(color)
        
    def build(self):
        # Process events (including checking for a quit event)
        self.eventList = pygame.event.get()
        for event in self.eventList:
            if event.type == pygame.QUIT:
                self.quit()
        delta = self.clock.tick(self.fps)
        pygame.display.update()

        return delta
    
    def drawTo(self, surface, coordinates):
        # Blit a given surface (image, text, etc.) onto the screen at specified coordinates
        self.screen.blit(surface, coordinates)
        
    def image(self, path):
        # Load an image with transparency support
        return pygame.image.load(path).convert_alpha()
        
    def groupedImage(self, path):
        # In this simple example, returns the same as image
        return pygame.image.load(path).convert_alpha()
        
    # --- Mouse and Keyboard Helper Functions ---
    def getMousePos(self):
        # Returns the current mouse position as a tuple (x, y)
        return pygame.mouse.get_pos()
    
    def mouseClicked(self, button=0):
        # Returns True if the specified mouse button is currently pressed
        pressed = pygame.mouse.get_pressed()
        return pressed[button]
    
    def keyPressed(self):
        # Returns a list representing the state of every key (True if pressed)
        return pygame.key.get_pressed()
    
    def getEvents(self):
        # Returns the list of events processed in the last call to build()
        return self.eventList

    def drawText(self, text, fontName, size, color, pos):
        # Utility function for rendering text
        font = pygame.font.Font(fontName, size)
        textSurface = font.render(text, True, color)
        self.screen.blit(textSurface, pos)


# --- Sound Management Class ---
class SoundManager:
    def __init__(self):
        # Initialize the mixer for sound
        pygame.mixer.init()
        self.sounds = {}
        self.musicVolume = 1.0
    
    def loadSound(self, name, path):
        # Load a sound file and assign it to a key for later reference
        sound = pygame.mixer.Sound(path)
        self.sounds[name] = sound
        return sound
    
    def playSound(self, name, loops=0):
        # Play a sound effect; loops=0 means play once, -1 loops indefinitely
        if name in self.sounds:
            self.sounds[name].play(loops=loops)
    
    def stopSound(self, name):
        # Stop a playing sound effect
        if name in self.sounds:
            self.sounds[name].stop()
    
    def playMusic(self, path, loops=-1):
        # Load and play background music. Default loops indefinitely.
        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.musicVolume)
        pygame.mixer.music.play(loops=loops)
    
    def stopMusic(self):
        pygame.mixer.music.stop()
    
    def setMusicVolume(self, volume):
        # Set the volume for music (0.0 to 1.0)
        self.musicVolume = volume
        pygame.mixer.music.set_volume(volume)
    
    def fadeoutMusic(self, timeMs):
        # Fade out the music over a given time in milliseconds
        pygame.mixer.music.fadeout(timeMs)


# --- Sprite and Collision Classes ---
class GradbitSprite(pygame.sprite.Sprite):
    def __init__(self, image, pos=(0, 0)):
        super().__init__()
        # Store the original image for transformations (rotation, scaling)
        self.originalImage = image
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        # Create a mask for pixel-perfect collision detection
        self.mask = pygame.mask.from_surface(self.image)
        
    def update(self, *args):
        # Custom update behavior can be defined here
        pass
    
    def rotate(self, angle):
        """Rotate sprite image and update its rect and collision mask."""
        self.image = pygame.transform.rotate(self.originalImage, angle)
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)
        self.mask = pygame.mask.from_surface(self.image)
    
    def scale(self, newSize):
        """Scale the sprite image to a new size (width, height) and update rect and mask."""
        self.image = pygame.transform.scale(self.originalImage, newSize)
        self.rect = self.image.get_rect(topleft=self.rect.topleft)
        self.mask = pygame.mask.from_surface(self.image)
        
    def collideWith(self, otherSprite):
        """
        Check for a pixel-perfect collision with another GradbitSprite.
        Returns True if collision is detected.
        """
        offset = (otherSprite.rect.left - self.rect.left, otherSprite.rect.top - self.rect.top)
        return self.mask.overlap(otherSprite.mask, offset) is not None
    
    def draw(self, surface):
        # Draw this sprite onto the provided surface
        surface.blit(self.image, self.rect)


class GradbitGroup(pygame.sprite.Group):
    """
    A group class for managing multiple GradbitSprites.
    It provides helper methods for collision detection and batch drawing.
    """
    def __init__(self, *sprites):
        super().__init__(*sprites)
    
    def update(self, *args):
        # Update all sprites in the group
        for sprite in self.sprites():
            sprite.update(*args)
    
    def draw(self, surface):
        # Draw all sprites onto the provided surface
        for sprite in self.sprites():
            sprite.draw(surface)
    
    def collisionCheck(self, sprite, doKill=False):
        """
        Check for rectangular collisions between a sprite and others in the group.
        If doKill is True, remove colliding sprites from the group.
        """
        return pygame.sprite.spritecollide(sprite, self, doKill)
    
    def pixelCollisionCheck(self, sprite, doKill=False):
        """
        Check for pixel-perfect collisions using masks.
        Returns a list of sprites that collided with the provided sprite.
        """
        collisions = []
        for s in self.sprites():
            if s is not sprite:
                offset = (s.rect.left - sprite.rect.left, s.rect.top - sprite.rect.top)
                if sprite.mask.overlap(s.mask, offset):
                    collisions.append(s)
                    if doKill:
                        s.kill()
        return collisions


# --- Mask Helper Functions ---
class MaskHelper:
    @staticmethod
    def createMaskFromImage(image):
        """Create and return a mask for the given image surface."""
        return pygame.mask.from_surface(image)
    
    @staticmethod
    def pixelPerfectCollision(sprite1, sprite2):
        """
        Check pixel-perfect collision between two sprites using their masks.
        Returns True if collision is detected.
        """
        offset = (sprite2.rect.left - sprite1.rect.left, sprite2.rect.top - sprite1.rect.top)
        return sprite1.mask.overlap(sprite2.mask, offset) is not None


# --- Timer Utility ---
class Timer:
    """
    A simple timer class to check if a specified interval has elapsed.
    Useful for managing delays or periodic events.
    """
    def __init__(self, interval):
        self.interval = interval  # in milliseconds
        self.lastTick = pygame.time.get_ticks()
    
    def ready(self):
        currentTick = pygame.time.get_ticks()
        if currentTick - self.lastTick >= self.interval:
            self.lastTick = currentTick
            return True
        
class Blackbody:
    def line(self, screen, color, start, end, width=1):
        pygame.draw.line(screen, color, start, end, width)

    def poly(screen, color, points, width=1):
        pygame.draw.polygon(screen, color, points, width)

    def circle(screen, color, center, radius, outline=0):
        pygame.draw.circle(screen, color, center, radius, outline)

    def rectangle(screen, color, rect, outline=0):
        pygame.draw.rect(screen, color, rect, outline)

class GradbitMouse:
    def hide():
        pygame.mouse.set_visible(False)

    def show():
        pygame.mouse.set_visible(True)

    def turn(on):
        pygame.mouse.set_visible(on)

    def pos(full=False):
        return pygame.mouse.get_pos(full)
    
    def setTo(pos):
        pygame.mouse.set_pos(pos)

    def click(number, full=False):
        pygame.mouse.get_pressed(number, full)

    def relative():
        return pygame.mouse.get_rel()