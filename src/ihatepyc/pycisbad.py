import asyncio
import os


class Watcher:
    """Watches your directory and subdirectories for __pycache__ folders and deletes them.

    Args:
        directory (str): The directory to watch.
        interval (int): The interval to check for __pycache__ folders.
        recursive (bool): Whether to watch subdirectories.
        verbose (bool): Whether to print verbose output.
    
    Attributes:
        directory (str): The directory to watch.
        interval (int): The interval to check for __pycache__ folders.
        recursive (bool): Whether to watch subdirectories.
        verbose (bool): Whether to print verbose output.
        loop (asyncio.AbstractEventLoop): The event loop.
        _running (bool): Whether the watcher is running.
    
    """
    
    def __init__(
        self,
        directory: str,
        interval: int = 1,
        recursive: bool = True,
        verbose: bool = False,
    ) -> None:
        self.directory = directory
        self.interval = interval
        self.recursive = recursive
        self.verbose = verbose
        self.loop = asyncio.get_event_loop()
        self._running = False

    async def _watch(self) -> None:
        """Watches the directory and subdirectories for __pycache__ folders and deletes them."""
        while self._running:
            # Checks for every __pycache__ folder in the directory and forcefully deletes them to avoid errors. this will skip any directories that have similar to venv folders.
            for root, dirs, files in os.walk(self.directory):
                for directory in dirs:
                    if directory == "__pycache__":
                        if self.verbose:
                            print(f"Deleting {os.path.join(root, directory)}")
                        os.system(f"rm -rf {os.path.join(root, directory)}")
            await asyncio.sleep(self.interval)

    def start(self) -> None:
        """Starts the watcher."""
        self._running = True
        self.loop.create_task(self._watch())
        self.loop.run_forever()

    def stop(self) -> None:
        """Stops the watcher."""
        self._running = False
        self.loop.stop()