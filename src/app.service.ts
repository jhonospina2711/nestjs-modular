import { Injectable, Inject } from '@nestjs/common';
import { ConfigService } from '@nestjs/config';
import { ConfigType } from '@nestjs/config';
import config from './config';

@Injectable()
export class AppService {
  constructor(
    // @Inject('API_KEY') private apiKey: string,
    @Inject('TASK') private task: any[],
    private config: ConfigService, //@Inject(config.KEY) private configService: ConfigType<typeof config>,
  ) {}
  getHello(): string {
    const apiKey = this.config.get('API_HEY');
    const databasename = this.config.get('DATABASE_NAME');
    //const apiKey = this.configService.apiKey;
    //const databasename = this.configService.database;
    return `Hello World! my apiKey is: ${apiKey} and my Data base name is: ${databasename}`;
  }
}
